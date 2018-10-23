# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manage_server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='manage_server.proto',
  package='build',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13manage_server.proto\x12\x05\x62uild\"l\n\x07\x43ommand\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x18.build.Command.ArgsEntry\x1a+\n\tArgsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x16\n\x06Result\x12\x0c\n\x04line\x18\x01 \x01(\t28\n\x06Manage\x12.\n\x0brun_command\x12\x0e.build.Command\x1a\r.build.Result0\x01\x62\x06proto3')
)




_COMMAND_ARGSENTRY = _descriptor.Descriptor(
  name='ArgsEntry',
  full_name='build.Command.ArgsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='build.Command.ArgsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='build.Command.ArgsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=138,
)

_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='build.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='build.Command.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='build.Command.args', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMMAND_ARGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=138,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='build.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='line', full_name='build.Result.line', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=162,
)

_COMMAND_ARGSENTRY.containing_type = _COMMAND
_COMMAND.fields_by_name['args'].message_type = _COMMAND_ARGSENTRY
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(

  ArgsEntry = _reflection.GeneratedProtocolMessageType('ArgsEntry', (_message.Message,), dict(
    DESCRIPTOR = _COMMAND_ARGSENTRY,
    __module__ = 'manage_server_pb2'
    # @@protoc_insertion_point(class_scope:build.Command.ArgsEntry)
    ))
  ,
  DESCRIPTOR = _COMMAND,
  __module__ = 'manage_server_pb2'
  # @@protoc_insertion_point(class_scope:build.Command)
  ))
_sym_db.RegisterMessage(Command)
_sym_db.RegisterMessage(Command.ArgsEntry)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'manage_server_pb2'
  # @@protoc_insertion_point(class_scope:build.Result)
  ))
_sym_db.RegisterMessage(Result)


_COMMAND_ARGSENTRY._options = None

_MANAGE = _descriptor.ServiceDescriptor(
  name='Manage',
  full_name='build.Manage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=164,
  serialized_end=220,
  methods=[
  _descriptor.MethodDescriptor(
    name='run_command',
    full_name='build.Manage.run_command',
    index=0,
    containing_service=None,
    input_type=_COMMAND,
    output_type=_RESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MANAGE)

DESCRIPTOR.services_by_name['Manage'] = _MANAGE

# @@protoc_insertion_point(module_scope)