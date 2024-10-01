# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from proto import visual_pb2 as proto_dot_visual__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in proto/visual_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class VisualServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateTimeSeries = channel.unary_unary(
                '/VisualService/GenerateTimeSeries',
                request_serializer=proto_dot_visual__pb2.TimeSeriesRequest.SerializeToString,
                response_deserializer=proto_dot_visual__pb2.ImageResponse.FromString,
                _registered_method=True)
        self.GenerateMonthlyAverage = channel.unary_unary(
                '/VisualService/GenerateMonthlyAverage',
                request_serializer=proto_dot_visual__pb2.DatasetRequest.SerializeToString,
                response_deserializer=proto_dot_visual__pb2.ImageResponse.FromString,
                _registered_method=True)
        self.GenerateVolumeAnalysis = channel.unary_unary(
                '/VisualService/GenerateVolumeAnalysis',
                request_serializer=proto_dot_visual__pb2.VolumeAnalysisRequest.SerializeToString,
                response_deserializer=proto_dot_visual__pb2.ImageResponse.FromString,
                _registered_method=True)
        self.GeneratePriceAndPercent = channel.unary_unary(
                '/VisualService/GeneratePriceAndPercent',
                request_serializer=proto_dot_visual__pb2.PriceAndPercentRequest.SerializeToString,
                response_deserializer=proto_dot_visual__pb2.ImageResponse.FromString,
                _registered_method=True)


class VisualServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GenerateTimeSeries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateMonthlyAverage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateVolumeAnalysis(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GeneratePriceAndPercent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VisualServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateTimeSeries': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateTimeSeries,
                    request_deserializer=proto_dot_visual__pb2.TimeSeriesRequest.FromString,
                    response_serializer=proto_dot_visual__pb2.ImageResponse.SerializeToString,
            ),
            'GenerateMonthlyAverage': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateMonthlyAverage,
                    request_deserializer=proto_dot_visual__pb2.DatasetRequest.FromString,
                    response_serializer=proto_dot_visual__pb2.ImageResponse.SerializeToString,
            ),
            'GenerateVolumeAnalysis': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateVolumeAnalysis,
                    request_deserializer=proto_dot_visual__pb2.VolumeAnalysisRequest.FromString,
                    response_serializer=proto_dot_visual__pb2.ImageResponse.SerializeToString,
            ),
            'GeneratePriceAndPercent': grpc.unary_unary_rpc_method_handler(
                    servicer.GeneratePriceAndPercent,
                    request_deserializer=proto_dot_visual__pb2.PriceAndPercentRequest.FromString,
                    response_serializer=proto_dot_visual__pb2.ImageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'VisualService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('VisualService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class VisualService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GenerateTimeSeries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/VisualService/GenerateTimeSeries',
            proto_dot_visual__pb2.TimeSeriesRequest.SerializeToString,
            proto_dot_visual__pb2.ImageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GenerateMonthlyAverage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/VisualService/GenerateMonthlyAverage',
            proto_dot_visual__pb2.DatasetRequest.SerializeToString,
            proto_dot_visual__pb2.ImageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GenerateVolumeAnalysis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/VisualService/GenerateVolumeAnalysis',
            proto_dot_visual__pb2.VolumeAnalysisRequest.SerializeToString,
            proto_dot_visual__pb2.ImageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GeneratePriceAndPercent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/VisualService/GeneratePriceAndPercent',
            proto_dot_visual__pb2.PriceAndPercentRequest.SerializeToString,
            proto_dot_visual__pb2.ImageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
