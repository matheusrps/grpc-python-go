import asyncio
from async_grpc_server import srv
from allocationPkg.grpc import run_grpc

if __name__ == "__main__":
    asyncio.run(run_grpc(srv, address="[::]:50051"))
