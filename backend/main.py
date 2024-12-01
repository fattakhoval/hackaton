import uvicorn
import asyncio

from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from src.routes.auth import auth_route
# from src.routes.user import user
from src.routes.category import category_route
from src.routes.transaction import transaction_route
from src.database.db_settings import engine
from src.database.models import BaseCRUD


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(BaseCRUD.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://0.0.0.0:3000",
        "http://frontend:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_route)
app.include_router(category_route)
app.include_router(transaction_route)


if __name__ == '__main__':

    uvicorn_config = uvicorn.Config(app, host='0.0.0.0', port=8485)
    server = uvicorn.Server(uvicorn_config)

    asyncio.run(server.serve())
