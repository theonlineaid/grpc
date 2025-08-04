# app/grpc_server.py

import grpc
from generated import user_pb2, user_pb2_grpc
from app.crud import create_user, get_user_by_id
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

class UserService(user_pb2_grpc.UserServiceServicer):
    async def CreateUser(self, request, context):
        async with get_db() as db:  # manually get db session
            user = await create_user(db, name=request.name, email=request.email)
            return user_pb2.UserReply(id=user.id, name=user.name, email=user.email)

    async def GetUser(self, request, context):
        async with get_db() as db:
            user = await get_user_by_id(db, request.id)
            if not user:
                context.abort(grpc.StatusCode.NOT_FOUND, "User not found")
            return user_pb2.UserReply(id=user.id, name=user.name, email=user.email)
