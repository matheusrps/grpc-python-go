import logging
import grpc


class GrpcServer:
    def __init__(self, service_registration_func, address="[::]:50051"):
        self.server = grpc.aio.server()
        self.service_registration_func = service_registration_func
        self.address = address

    async def start(self):
        self.service_registration_func(self.server)
        self.server.add_insecure_port(self.address)
        logging.info("Starting server on %s", self.address)
        await self.server.start()

    async def stop(self):
        await self.server.stop(None)

    async def run(self):
        await self.start()
        await self.server.wait_for_termination()


async def run_grpc(srv, address="[::]:50051"):
    logging.basicConfig(level=logging.INFO)
    server = GrpcServer(srv, address)
    await server.run()
