import grpc
import asyncio
import logging
from protos import helloworld_pb2, helloworld_pb2_grpc
from allocationPkg.grpc import GrpcServer, run_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    async def SayHello(
            self,
            request: helloworld_pb2.HelloRequest,
            context: grpc.aio.ServicerContext,
    ) -> helloworld_pb2.HelloReply:
        await asyncio.sleep(10)
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)


srv = lambda server: helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

