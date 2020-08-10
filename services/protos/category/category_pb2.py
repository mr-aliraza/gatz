# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: category.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='category.proto',
  package='user',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x63\x61tegory.proto\x12\x04user\x1a\x1bgoogle/protobuf/empty.proto\"\xa3\x01\n\x08\x43\x61tegory\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tparent_id\x18\x04 \x01(\t\x12\x13\n\x0bparent_name\x18\x05 \x01(\t\x12\x0f\n\x07user_id\x18\x06 \x01(\x05\x12\x0e\n\x06status\x18\x07 \x01(\x05\x12\x0e\n\x06result\x18\x08 \x01(\t\x12\x0f\n\x07message\x18\t \x01(\t\"\x15\n\x13\x43\x61tegoryListRequest\"%\n\x17\x43\x61tegoryRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\t\"4\n\x15\x43\x61tegoryDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\"J\n\x11\x43\x61tegoryAttribute\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61tegory_id\x18\x02 \x01(\t\x12\x14\n\x0c\x61ttribute_id\x18\x03 \x01(\t\"3\n\x1c\x43\x61tegoryAttributeListRequest\x12\x13\n\x0b\x63\x61tegory_id\x18\x01 \x01(\t\".\n CategoryAttributeRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\t\"F\n\x0f\x43\x61tegoryVariant\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61tegory_id\x18\x02 \x01(\t\x12\x12\n\nvariant_id\x18\x03 \x01(\t\"1\n\x1a\x43\x61tegoryVariantListRequest\x12\x13\n\x0b\x63\x61tegory_id\x18\x01 \x01(\t\",\n\x1e\x43\x61tegoryVariantRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\t2\xa1\x03\n\x12\x43\x61tegoryController\x12\x35\n\x04List\x12\x19.user.CategoryListRequest\x1a\x0e.user.Category\"\x00\x30\x01\x12*\n\x06\x43reate\x12\x0e.user.Category\x1a\x0e.user.Category\"\x00\x12;\n\x08Retrieve\x12\x1d.user.CategoryRetrieveRequest\x1a\x0e.user.Category\"\x00\x12@\n\x0fRetrieveParents\x12\x19.user.CategoryListRequest\x1a\x0e.user.Category\"\x00\x30\x01\x12\x43\n\x0eRetrieveChilds\x12\x1d.user.CategoryRetrieveRequest\x1a\x0e.user.Category\"\x00\x30\x01\x12*\n\x06Update\x12\x0e.user.Category\x1a\x0e.user.Category\"\x00\x12\x38\n\x07\x44\x65stroy\x12\x1b.user.CategoryDeleteRequest\x1a\x0e.user.Category\"\x00\x32\xef\x02\n\x1b\x43\x61tegoryAttributeController\x12G\n\x04List\x12\".user.CategoryAttributeListRequest\x1a\x17.user.CategoryAttribute\"\x00\x30\x01\x12<\n\x06\x43reate\x12\x17.user.CategoryAttribute\x1a\x17.user.CategoryAttribute\"\x00\x12M\n\x08Retrieve\x12&.user.CategoryAttributeRetrieveRequest\x1a\x17.user.CategoryAttribute\"\x00\x12<\n\x06Update\x12\x17.user.CategoryAttribute\x1a\x17.user.CategoryAttribute\"\x00\x12<\n\x07\x44\x65stroy\x12\x17.user.CategoryAttribute\x1a\x16.google.protobuf.Empty\"\x00\x32\xdb\x02\n\x19\x43\x61tegoryVariantController\x12\x43\n\x04List\x12 .user.CategoryVariantListRequest\x1a\x15.user.CategoryVariant\"\x00\x30\x01\x12\x38\n\x06\x43reate\x12\x15.user.CategoryVariant\x1a\x15.user.CategoryVariant\"\x00\x12I\n\x08Retrieve\x12$.user.CategoryVariantRetrieveRequest\x1a\x15.user.CategoryVariant\"\x00\x12\x38\n\x06Update\x12\x15.user.CategoryVariant\x1a\x15.user.CategoryVariant\"\x00\x12:\n\x07\x44\x65stroy\x12\x15.user.CategoryVariant\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_CATEGORY = _descriptor.Descriptor(
  name='Category',
  full_name='user.Category',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.Category.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='user.Category.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='user.Category.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='user.Category.parent_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_name', full_name='user.Category.parent_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='user.Category.user_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='user.Category.status', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='user.Category.result', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='user.Category.message', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=54,
  serialized_end=217,
)


_CATEGORYLISTREQUEST = _descriptor.Descriptor(
  name='CategoryListRequest',
  full_name='user.CategoryListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=219,
  serialized_end=240,
)


_CATEGORYRETRIEVEREQUEST = _descriptor.Descriptor(
  name='CategoryRetrieveRequest',
  full_name='user.CategoryRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.CategoryRetrieveRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=242,
  serialized_end=279,
)


_CATEGORYDELETEREQUEST = _descriptor.Descriptor(
  name='CategoryDeleteRequest',
  full_name='user.CategoryDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.CategoryDeleteRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='user.CategoryDeleteRequest.user_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=281,
  serialized_end=333,
)


_CATEGORYATTRIBUTE = _descriptor.Descriptor(
  name='CategoryAttribute',
  full_name='user.CategoryAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.CategoryAttribute.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category_id', full_name='user.CategoryAttribute.category_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribute_id', full_name='user.CategoryAttribute.attribute_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=335,
  serialized_end=409,
)


_CATEGORYATTRIBUTELISTREQUEST = _descriptor.Descriptor(
  name='CategoryAttributeListRequest',
  full_name='user.CategoryAttributeListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category_id', full_name='user.CategoryAttributeListRequest.category_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=411,
  serialized_end=462,
)


_CATEGORYATTRIBUTERETRIEVEREQUEST = _descriptor.Descriptor(
  name='CategoryAttributeRetrieveRequest',
  full_name='user.CategoryAttributeRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.CategoryAttributeRetrieveRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=464,
  serialized_end=510,
)


_CATEGORYVARIANT = _descriptor.Descriptor(
  name='CategoryVariant',
  full_name='user.CategoryVariant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.CategoryVariant.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category_id', full_name='user.CategoryVariant.category_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='variant_id', full_name='user.CategoryVariant.variant_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=512,
  serialized_end=582,
)


_CATEGORYVARIANTLISTREQUEST = _descriptor.Descriptor(
  name='CategoryVariantListRequest',
  full_name='user.CategoryVariantListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category_id', full_name='user.CategoryVariantListRequest.category_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=584,
  serialized_end=633,
)


_CATEGORYVARIANTRETRIEVEREQUEST = _descriptor.Descriptor(
  name='CategoryVariantRetrieveRequest',
  full_name='user.CategoryVariantRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.CategoryVariantRetrieveRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=635,
  serialized_end=679,
)

DESCRIPTOR.message_types_by_name['Category'] = _CATEGORY
DESCRIPTOR.message_types_by_name['CategoryListRequest'] = _CATEGORYLISTREQUEST
DESCRIPTOR.message_types_by_name['CategoryRetrieveRequest'] = _CATEGORYRETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['CategoryDeleteRequest'] = _CATEGORYDELETEREQUEST
DESCRIPTOR.message_types_by_name['CategoryAttribute'] = _CATEGORYATTRIBUTE
DESCRIPTOR.message_types_by_name['CategoryAttributeListRequest'] = _CATEGORYATTRIBUTELISTREQUEST
DESCRIPTOR.message_types_by_name['CategoryAttributeRetrieveRequest'] = _CATEGORYATTRIBUTERETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['CategoryVariant'] = _CATEGORYVARIANT
DESCRIPTOR.message_types_by_name['CategoryVariantListRequest'] = _CATEGORYVARIANTLISTREQUEST
DESCRIPTOR.message_types_by_name['CategoryVariantRetrieveRequest'] = _CATEGORYVARIANTRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Category = _reflection.GeneratedProtocolMessageType('Category', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORY,
  '__module__' : 'category_pb2'
  # @@protoc_insertion_point(class_scope:user.Category)
  })
_sym_db.RegisterMessage(Category)

CategoryListRequest = _reflection.GeneratedProtocolMessageType('CategoryListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYLISTREQUEST,
  '__module__' : 'category_pb2'
  # @@protoc_insertion_point(class_scope:user.CategoryListRequest)
  })
_sym_db.RegisterMessage(CategoryListRequest)

CategoryRetrieveRequest = _reflection.GeneratedProtocolMessageType('CategoryRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYRETRIEVEREQUEST,
  '__module__' : 'category_pb2'
  # @@protoc_insertion_point(class_scope:user.CategoryRetrieveRequest)
  })
_sym_db.RegisterMessage(CategoryRetrieveRequest)

CategoryDeleteRequest = _reflection.GeneratedProtocolMessageType('CategoryDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYDELETEREQUEST,
  '__module__' : 'category_pb2'
  # @@protoc_insertion_point(class_scope:user.CategoryDeleteRequest)
  })
_sym_db.RegisterMessage(CategoryDeleteRequest)

CategoryAttribute = _reflection.GeneratedProtocolMessageType('CategoryAttribute', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYATTRIBUTE,
  '__module__' : 'category_pb2'
  # @@protoc_insertion_point(class_scope:user.CategoryAttribute)
  })
_sym_db.RegisterMessage(CategoryAttribute)

CategoryAttributeListRequest = _reflection.GeneratedProtocolMessageType('CategoryAttributeListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYATTRIBUTELISTREQUEST,
  '__module__' : 'category_pb2'
  # @@protoc_insertion_point(class_scope:user.CategoryAttributeListRequest)
  })
_sym_db.RegisterMessage(CategoryAttributeListRequest)

CategoryAttributeRetrieveRequest = _reflection.GeneratedProtocolMessageType('CategoryAttributeRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYATTRIBUTERETRIEVEREQUEST,
  '__module__' : 'category_pb2'
  # @@protoc_insertion_point(class_scope:user.CategoryAttributeRetrieveRequest)
  })
_sym_db.RegisterMessage(CategoryAttributeRetrieveRequest)

CategoryVariant = _reflection.GeneratedProtocolMessageType('CategoryVariant', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYVARIANT,
  '__module__' : 'category_pb2'
  # @@protoc_insertion_point(class_scope:user.CategoryVariant)
  })
_sym_db.RegisterMessage(CategoryVariant)

CategoryVariantListRequest = _reflection.GeneratedProtocolMessageType('CategoryVariantListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYVARIANTLISTREQUEST,
  '__module__' : 'category_pb2'
  # @@protoc_insertion_point(class_scope:user.CategoryVariantListRequest)
  })
_sym_db.RegisterMessage(CategoryVariantListRequest)

CategoryVariantRetrieveRequest = _reflection.GeneratedProtocolMessageType('CategoryVariantRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYVARIANTRETRIEVEREQUEST,
  '__module__' : 'category_pb2'
  # @@protoc_insertion_point(class_scope:user.CategoryVariantRetrieveRequest)
  })
_sym_db.RegisterMessage(CategoryVariantRetrieveRequest)



_CATEGORYCONTROLLER = _descriptor.ServiceDescriptor(
  name='CategoryController',
  full_name='user.CategoryController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=682,
  serialized_end=1099,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='user.CategoryController.List',
    index=0,
    containing_service=None,
    input_type=_CATEGORYLISTREQUEST,
    output_type=_CATEGORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='user.CategoryController.Create',
    index=1,
    containing_service=None,
    input_type=_CATEGORY,
    output_type=_CATEGORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='user.CategoryController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_CATEGORYRETRIEVEREQUEST,
    output_type=_CATEGORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RetrieveParents',
    full_name='user.CategoryController.RetrieveParents',
    index=3,
    containing_service=None,
    input_type=_CATEGORYLISTREQUEST,
    output_type=_CATEGORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RetrieveChilds',
    full_name='user.CategoryController.RetrieveChilds',
    index=4,
    containing_service=None,
    input_type=_CATEGORYRETRIEVEREQUEST,
    output_type=_CATEGORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='user.CategoryController.Update',
    index=5,
    containing_service=None,
    input_type=_CATEGORY,
    output_type=_CATEGORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='user.CategoryController.Destroy',
    index=6,
    containing_service=None,
    input_type=_CATEGORYDELETEREQUEST,
    output_type=_CATEGORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CATEGORYCONTROLLER)

DESCRIPTOR.services_by_name['CategoryController'] = _CATEGORYCONTROLLER


_CATEGORYATTRIBUTECONTROLLER = _descriptor.ServiceDescriptor(
  name='CategoryAttributeController',
  full_name='user.CategoryAttributeController',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1102,
  serialized_end=1469,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='user.CategoryAttributeController.List',
    index=0,
    containing_service=None,
    input_type=_CATEGORYATTRIBUTELISTREQUEST,
    output_type=_CATEGORYATTRIBUTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='user.CategoryAttributeController.Create',
    index=1,
    containing_service=None,
    input_type=_CATEGORYATTRIBUTE,
    output_type=_CATEGORYATTRIBUTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='user.CategoryAttributeController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_CATEGORYATTRIBUTERETRIEVEREQUEST,
    output_type=_CATEGORYATTRIBUTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='user.CategoryAttributeController.Update',
    index=3,
    containing_service=None,
    input_type=_CATEGORYATTRIBUTE,
    output_type=_CATEGORYATTRIBUTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='user.CategoryAttributeController.Destroy',
    index=4,
    containing_service=None,
    input_type=_CATEGORYATTRIBUTE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CATEGORYATTRIBUTECONTROLLER)

DESCRIPTOR.services_by_name['CategoryAttributeController'] = _CATEGORYATTRIBUTECONTROLLER


_CATEGORYVARIANTCONTROLLER = _descriptor.ServiceDescriptor(
  name='CategoryVariantController',
  full_name='user.CategoryVariantController',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1472,
  serialized_end=1819,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='user.CategoryVariantController.List',
    index=0,
    containing_service=None,
    input_type=_CATEGORYVARIANTLISTREQUEST,
    output_type=_CATEGORYVARIANT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='user.CategoryVariantController.Create',
    index=1,
    containing_service=None,
    input_type=_CATEGORYVARIANT,
    output_type=_CATEGORYVARIANT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='user.CategoryVariantController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_CATEGORYVARIANTRETRIEVEREQUEST,
    output_type=_CATEGORYVARIANT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='user.CategoryVariantController.Update',
    index=3,
    containing_service=None,
    input_type=_CATEGORYVARIANT,
    output_type=_CATEGORYVARIANT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='user.CategoryVariantController.Destroy',
    index=4,
    containing_service=None,
    input_type=_CATEGORYVARIANT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CATEGORYVARIANTCONTROLLER)

DESCRIPTOR.services_by_name['CategoryVariantController'] = _CATEGORYVARIANTCONTROLLER

# @@protoc_insertion_point(module_scope)
