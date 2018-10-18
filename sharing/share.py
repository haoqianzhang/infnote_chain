from threading import Thread
from networking import Peer, Message, Server, PeerManager
from .sentence import Sentence, Info
from .factory import SentenceFactory as Factory

from utils.logger import default_logger as log


class ShareManager:
    def __init__(self):
        self.servers = [peer for peer in PeerManager().peers(without_self=True) if peer.address]
        self.clients = []
        self.boardcast_cache = {}

    def start(self):
        for peer in self.servers:
            peer.peer_in = self.peer_in
            peer.peer_out = self.peer_out
            Thread(target=peer.open).start()

        server = Server()
        server.peer_in = self.peer_in
        server.peer_out = self.peer_out
        Thread(target=server.start).start()

    def refresh(self):
        # TODO: need a connection strategy (when current connections is less then specific number)
        pass

    async def peer_in(self, peer):
        log.info(f'Peer in : {peer}')
        peer.dispatcher.global_handler = self.handle
        if peer.is_server:
            await peer.send(Info().question)
        else:
            self.clients.append(peer)

    async def peer_out(self, peer):
        log.info(f'Peer out: {peer}')
        if peer.is_server:
            self.servers.remove(peer)
        else:
            self.clients.remove(peer)
        self.refresh()

    async def handle(self, message: Message, peer: Peer):
        sentence = Factory.load(message)
        if sentence is None:
            log.warn(f'Bad sentence:\n{message.content}')

        if message.type == Message.Type.QUESTION:
            await self.handle_question(sentence, peer)
        elif message.type == Message.Type.ANSWER:
            await self.handle_anwser(sentence, peer)

    async def handle_question(self, question, peer: Peer):
        log.debug(f'Legal Question from {peer}:\n{question}')

        answer = None
        if question.type == Sentence.Type.NEW_BLOCK:
            wb = Factory.want_blocks_for_new_block(question)
            if wb is not None:
                await peer.send(wb.question)
            if self.boardcast_cache.get(question.message.identifer) is None:
                self.boardcast_cache[question.message.identifer] = question
                await self.boardcast(question, peer)
            return
        elif question.type == Sentence.Type.INFO:
            answer = Info()
            if answer is not None:
                await peer.send(Info().to(question))
                await self.info_actions(question, peer)
            return
        elif question.type == Sentence.Type.WANT_BLOCKS:
            answer = Factory.send_blocks(question)
        elif question.type == Sentence.Type.WANT_PEERS:
            answer = Factory.send_peers(question)

        if answer is not None:
            await peer.send(answer.to(question))

    async def handle_anwser(self, answer, peer: Peer):
        log.debug(f'Legal Answer from {peer}:\n{answer}')

        if answer.type == Sentence.Type.INFO:
            await self.info_actions(answer, peer)
        elif answer.type == Sentence.Type.BLOCKS:
            Factory.handle_blocks(answer)
        elif answer.type == Sentence.Type.PEERS:
            Factory.handle_peers(answer)

    async def boardcast(self, sentence, without=None):
        log.debug(f'Boardcasting:\n{sentence}')
        for peer in self.servers + self.clients:
            if without is not None and peer.address == without.address and peer.port == without.port:
                continue
            await peer.send(sentence.question)

    @staticmethod
    async def info_actions(info: Info, peer: Peer):
        if isinstance(info, Message):
            info = Factory.load(info)
        if info is None:
            return

        for want_blocks in Factory.want_blocks_for_info(info):
            await peer.send(want_blocks.question)

        want_peers = Factory.want_peers_for_info(info)
        if want_peers is not None:
            await peer.send(want_peers.question)
