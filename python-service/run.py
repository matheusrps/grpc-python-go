import asyncio
from async_grpc_server import srv
from allocationPkg.grpc import runGrpc

if __name__ == "__main__":
    asyncio.run(runGrpc(srv, address="[::]:50051"))
