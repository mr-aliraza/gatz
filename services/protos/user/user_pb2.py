# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='user.proto',
  package='user',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nuser.proto\x12\x04user\x1a\x1bgoogle/protobuf/empty.proto\"\xc2\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x0e\n\x06mobile\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x10\n\x08password\x18\x06 \x01(\t\x12\x0e\n\x06gender\x18\x07 \x01(\t\x12\x15\n\rdate_of_birth\x18\x08 \x01(\t\x12\x11\n\tis_active\x18\t \x01(\x08\x12\x0e\n\x06status\x18\n \x01(\x05\x12\x0c\n\x04role\x18\x0b \x01(\x05\"\x11\n\x0fUserListRequest\"!\n\x13UserRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\xed\x01\n\x0eUserController\x12-\n\x04List\x12\x15.user.UserListRequest\x1a\n.user.User\"\x00\x30\x01\x12\"\n\x06\x43reate\x12\n.user.User\x1a\n.user.User\"\x00\x12\x33\n\x08Retrieve\x12\x19.user.UserRetrieveRequest\x1a\n.user.User\"\x00\x12\"\n\x06Update\x12\n.user.User\x1a\n.user.User\"\x00\x12/\n\x07\x44\x65stroy\x12\n.user.User\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_USER = _descriptor.Descriptor(
  name='User',
  full_name='user.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.User.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='user.User.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='user.User.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobile', full_name='user.User.mobile', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='user.User.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='user.User.password', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='user.User.gender', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_of_birth', full_name='user.User.date_of_birth', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_active', full_name='user.User.is_active', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='user.User.status', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='user.User.role', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=50,
  serialized_end=244,
)


_USERLISTREQUEST = _descriptor.Descriptor(
  name='UserListRequest',
  full_name='user.UserListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=246,
  serialized_end=263,
)


_USERRETRIEVEREQUEST = _descriptor.Descriptor(
  name='UserRetrieveRequest',
  full_name='user.UserRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.UserRetrieveRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=265,
  serialized_end=298,
)

DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['UserListRequest'] = _USERLISTREQUEST
DESCRIPTOR.message_types_by_name['UserRetrieveRequest'] = _USERRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.User)
  })
_sym_db.RegisterMessage(User)

UserListRequest = _reflection.GeneratedProtocolMessageType('UserListRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERLISTREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserListRequest)
  })
_sym_db.RegisterMessage(UserListRequest)

UserRetrieveRequest = _reflection.GeneratedProtocolMessageType('UserRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERRETRIEVEREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserRetrieveRequest)
  })
_sym_db.RegisterMessage(UserRetrieveRequest)



_USERCONTROLLER = _descriptor.ServiceDescriptor(
  name='UserController',
  full_name='user.UserController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=301,
  serialized_end=538,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='user.UserController.List',
    index=0,
    containing_service=None,
    input_type=_USERLISTREQUEST,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='user.UserController.Create',
    index=1,
    containing_service=None,
    input_type=_USER,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='user.UserController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_USERRETRIEVEREQUEST,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='user.UserController.Update',
    index=3,
    containing_service=None,
    input_type=_USER,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='user.UserController.Destroy',
    index=4,
    containing_service=None,
    input_type=_USER,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERCONTROLLER)

DESCRIPTOR.services_by_name['UserController'] = _USERCONTROLLER

# @@protoc_insertion_point(module_scope)
