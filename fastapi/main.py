import logging

from redis import asyncio as aioredis
import uvicorn as uvicorn
from api.v1 import endpoints
from core.config import settings
from core.logger import LOGGING
import db

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


app = FastAPI(
    title=settings.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    version="1.0.0",
)


@app.on_event("startup")
async def startup():
    db.redis = await aioredis.from_url(
        settings.redis_dsn,
        max_connections=10,
        encoding="utf8",
        decode_responses=True,
    )


@app.on_event("shutdown")
async def shutdown():
    await db.redis.close()


app.include_router(
    endpoints.router,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
