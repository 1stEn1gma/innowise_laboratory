from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from books.router import router as router_books
from books.database import engine, metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create tables in the database before startup and closes access to database after shutdown"""
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(
    title="TDL",
    lifespan=lifespan,
    responses={
        500: {"description": "Internal Server Error"}
    }
)


origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


app.include_router(router_books)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
