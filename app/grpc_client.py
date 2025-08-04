import grpc
from generated import user_pb2, user_pb2_grpc

async def get_user_from_grpc(user_id: int):
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        request = user_pb2.UserRequest(id=user_id)
        response = await stub.GetUser(request)
        return response
