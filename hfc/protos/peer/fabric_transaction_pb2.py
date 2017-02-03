# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/peer/fabric_transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/peer/fabric_transaction.proto',
  package='hfc.protos.peer',
  syntax='proto3',
  serialized_pb=_b('\n(hfc/protos/peer/fabric_transaction.proto\x12\x0fhfc.protos.peer\x1a\x1fgoogle/protobuf/timestamp.proto\"@\n\x11SignedTransaction\x12\x18\n\x10transactionBytes\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"\xbd\x01\n\x12InvalidTransaction\x12\x31\n\x0btransaction\x18\x01 \x01(\x0b\x32\x1c.hfc.protos.peer.Transaction\x12\x38\n\x05\x63\x61use\x18\x02 \x01(\x0e\x32).hfc.protos.peer.InvalidTransaction.Cause\":\n\x05\x43\x61use\x12\x15\n\x11TxIdAlreadyExists\x10\x00\x12\x1a\n\x16RWConflictDuringCommit\x10\x01\"\x82\x01\n\x0bTransaction\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x07\x61\x63tions\x18\x03 \x03(\x0b\x32\".hfc.protos.peer.TransactionAction\"4\n\x11TransactionAction\x12\x0e\n\x06header\x18\x01 \x01(\x0c\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x42+Z)github.com/hyperledger/fabric/protos/peerb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_INVALIDTRANSACTION_CAUSE = _descriptor.EnumDescriptor(
  name='Cause',
  full_name='hfc.protos.peer.InvalidTransaction.Cause',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TxIdAlreadyExists', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RWConflictDuringCommit', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=292,
  serialized_end=350,
)
_sym_db.RegisterEnumDescriptor(_INVALIDTRANSACTION_CAUSE)


_SIGNEDTRANSACTION = _descriptor.Descriptor(
  name='SignedTransaction',
  full_name='hfc.protos.peer.SignedTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactionBytes', full_name='hfc.protos.peer.SignedTransaction.transactionBytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='hfc.protos.peer.SignedTransaction.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=158,
)


_INVALIDTRANSACTION = _descriptor.Descriptor(
  name='InvalidTransaction',
  full_name='hfc.protos.peer.InvalidTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='hfc.protos.peer.InvalidTransaction.transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cause', full_name='hfc.protos.peer.InvalidTransaction.cause', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INVALIDTRANSACTION_CAUSE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=350,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='hfc.protos.peer.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='hfc.protos.peer.Transaction.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='hfc.protos.peer.Transaction.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actions', full_name='hfc.protos.peer.Transaction.actions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=353,
  serialized_end=483,
)


_TRANSACTIONACTION = _descriptor.Descriptor(
  name='TransactionAction',
  full_name='hfc.protos.peer.TransactionAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='hfc.protos.peer.TransactionAction.header', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='hfc.protos.peer.TransactionAction.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=485,
  serialized_end=537,
)

_INVALIDTRANSACTION.fields_by_name['transaction'].message_type = _TRANSACTION
_INVALIDTRANSACTION.fields_by_name['cause'].enum_type = _INVALIDTRANSACTION_CAUSE
_INVALIDTRANSACTION_CAUSE.containing_type = _INVALIDTRANSACTION
_TRANSACTION.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRANSACTION.fields_by_name['actions'].message_type = _TRANSACTIONACTION
DESCRIPTOR.message_types_by_name['SignedTransaction'] = _SIGNEDTRANSACTION
DESCRIPTOR.message_types_by_name['InvalidTransaction'] = _INVALIDTRANSACTION
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['TransactionAction'] = _TRANSACTIONACTION

SignedTransaction = _reflection.GeneratedProtocolMessageType('SignedTransaction', (_message.Message,), dict(
  DESCRIPTOR = _SIGNEDTRANSACTION,
  __module__ = 'hfc.protos.peer.fabric_transaction_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.SignedTransaction)
  ))
_sym_db.RegisterMessage(SignedTransaction)

InvalidTransaction = _reflection.GeneratedProtocolMessageType('InvalidTransaction', (_message.Message,), dict(
  DESCRIPTOR = _INVALIDTRANSACTION,
  __module__ = 'hfc.protos.peer.fabric_transaction_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.InvalidTransaction)
  ))
_sym_db.RegisterMessage(InvalidTransaction)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'hfc.protos.peer.fabric_transaction_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

TransactionAction = _reflection.GeneratedProtocolMessageType('TransactionAction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONACTION,
  __module__ = 'hfc.protos.peer.fabric_transaction_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.TransactionAction)
  ))
_sym_db.RegisterMessage(TransactionAction)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/hyperledger/fabric/protos/peer'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
