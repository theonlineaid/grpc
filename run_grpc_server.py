# run_grpc_server.py

import asyncio
import grpc
from concurrent import futures
from generated import user_pb2_grpc
from app.grpc_server import UserService

async def serve():
    server = grpc.aio.server()
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    print("✅ gRPC Server running at :50051")
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())
