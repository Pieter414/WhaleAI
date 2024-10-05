# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/visual.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'proto/visual.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12proto/visual.proto\"D\n\x11TimeSeriesRequest\x12\x0f\n\x07\x64\x61taset\x18\x01 \x01(\t\x12\n\n\x02mv\x18\x02 \x01(\x05\x12\x12\n\ndate_range\x18\x03 \x01(\t\"<\n\x15VolumeAnalysisRequest\x12\x0f\n\x07\x64\x61taset\x18\x01 \x01(\t\x12\x12\n\ndate_range\x18\x02 \x01(\t\"=\n\x16PriceAndPercentRequest\x12\x0f\n\x07\x64\x61taset\x18\x01 \x01(\t\x12\x12\n\ndate_range\x18\x02 \x01(\t\"!\n\x0e\x44\x61tasetRequest\x12\x0f\n\x07\x64\x61taset\x18\x01 \x01(\t\"#\n\rImageResponse\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\"!\n\x0cJsonResponse\x12\x11\n\tjson_data\x18\x01 \x01(\t2\x87\x02\n\rVisualService\x12\x37\n\x12GenerateTimeSeries\x12\x12.TimeSeriesRequest\x1a\r.JsonResponse\x12\x39\n\x16GenerateMonthlyAverage\x12\x0f.DatasetRequest\x1a\x0e.ImageResponse\x12?\n\x16GenerateVolumeAnalysis\x12\x16.VolumeAnalysisRequest\x1a\r.JsonResponse\x12\x41\n\x17GeneratePriceAndPercent\x12\x17.PriceAndPercentRequest\x1a\r.JsonResponseB\tZ\x07./protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.visual_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\007./proto'
  _globals['_TIMESERIESREQUEST']._serialized_start=22
  _globals['_TIMESERIESREQUEST']._serialized_end=90
  _globals['_VOLUMEANALYSISREQUEST']._serialized_start=92
  _globals['_VOLUMEANALYSISREQUEST']._serialized_end=152
  _globals['_PRICEANDPERCENTREQUEST']._serialized_start=154
  _globals['_PRICEANDPERCENTREQUEST']._serialized_end=215
  _globals['_DATASETREQUEST']._serialized_start=217
  _globals['_DATASETREQUEST']._serialized_end=250
  _globals['_IMAGERESPONSE']._serialized_start=252
  _globals['_IMAGERESPONSE']._serialized_end=287
  _globals['_JSONRESPONSE']._serialized_start=289
  _globals['_JSONRESPONSE']._serialized_end=322
  _globals['_VISUALSERVICE']._serialized_start=325
  _globals['_VISUALSERVICE']._serialized_end=588
# @@protoc_insertion_point(module_scope)
