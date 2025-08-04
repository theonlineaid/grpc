# File structure

```
grpc_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI app
│   ├── models.py              # SQLAlchemy Models
│   ├── crud.py                # DB logic
│   ├── database.py            # DB engine/session
│   ├── grpc_server.py         # gRPC server
│   └── grpc_client.py         # gRPC client for FastAPI
├── protos/
│   └── user.proto             # gRPC schema
├── generated/
│   ├── user_pb2.py
│   └── user_pb2_grpc.py
├── requirements.txt
└── run_grpc_server.py         # gRPC Server Runner
```