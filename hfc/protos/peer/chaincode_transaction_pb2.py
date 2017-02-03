# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/peer/chaincode_transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hfc.protos.peer import fabric_proposal_response_pb2 as hfc_dot_protos_dot_peer_dot_fabric__proposal__response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/peer/chaincode_transaction.proto',
  package='hfc.protos.peer',
  syntax='proto3',
  serialized_pb=_b('\n+hfc/protos/peer/chaincode_transaction.proto\x12\x0fhfc.protos.peer\x1a.hfc/protos/peer/fabric_proposal_response.proto\"t\n\x16\x43haincodeActionPayload\x12 \n\x18\x63haincodeProposalPayload\x18\x01 \x01(\x0c\x12\x38\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32(.hfc.protos.peer.ChaincodeEndorsedAction\"n\n\x17\x43haincodeEndorsedAction\x12\x1f\n\x17proposalResponsePayload\x18\x01 \x01(\x0c\x12\x32\n\x0c\x65ndorsements\x18\x02 \x03(\x0b\x32\x1c.hfc.protos.peer.EndorsementB+Z)github.com/hyperledger/fabric/protos/peerb\x06proto3')
  ,
  dependencies=[hfc_dot_protos_dot_peer_dot_fabric__proposal__response__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHAINCODEACTIONPAYLOAD = _descriptor.Descriptor(
  name='ChaincodeActionPayload',
  full_name='hfc.protos.peer.ChaincodeActionPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincodeProposalPayload', full_name='hfc.protos.peer.ChaincodeActionPayload.chaincodeProposalPayload', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='hfc.protos.peer.ChaincodeActionPayload.action', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=112,
  serialized_end=228,
)


_CHAINCODEENDORSEDACTION = _descriptor.Descriptor(
  name='ChaincodeEndorsedAction',
  full_name='hfc.protos.peer.ChaincodeEndorsedAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposalResponsePayload', full_name='hfc.protos.peer.ChaincodeEndorsedAction.proposalResponsePayload', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endorsements', full_name='hfc.protos.peer.ChaincodeEndorsedAction.endorsements', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=230,
  serialized_end=340,
)

_CHAINCODEACTIONPAYLOAD.fields_by_name['action'].message_type = _CHAINCODEENDORSEDACTION
_CHAINCODEENDORSEDACTION.fields_by_name['endorsements'].message_type = hfc_dot_protos_dot_peer_dot_fabric__proposal__response__pb2._ENDORSEMENT
DESCRIPTOR.message_types_by_name['ChaincodeActionPayload'] = _CHAINCODEACTIONPAYLOAD
DESCRIPTOR.message_types_by_name['ChaincodeEndorsedAction'] = _CHAINCODEENDORSEDACTION

ChaincodeActionPayload = _reflection.GeneratedProtocolMessageType('ChaincodeActionPayload', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEACTIONPAYLOAD,
  __module__ = 'hfc.protos.peer.chaincode_transaction_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.ChaincodeActionPayload)
  ))
_sym_db.RegisterMessage(ChaincodeActionPayload)

ChaincodeEndorsedAction = _reflection.GeneratedProtocolMessageType('ChaincodeEndorsedAction', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEENDORSEDACTION,
  __module__ = 'hfc.protos.peer.chaincode_transaction_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.ChaincodeEndorsedAction)
  ))
_sym_db.RegisterMessage(ChaincodeEndorsedAction)


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
