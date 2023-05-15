from functools import lru_cache
from typing import Optional

from fastapi import Depends
from redis import asyncio as aioredis

from db import get_redis
from models import Data

BASE_CACHE_EXPIRE_IN_SECONDS = 60 * 5  # время хранения 5 минут


class DataService:
    def __init__(self, redis: aioredis.Redis):
        self.redis = redis

    async def get_from_cache(self, key: str) -> Optional[Data]:
        """Получение данных в БД"""
        data = await self.redis.get(key)
        if not data:
            return None
        return Data.parse_raw(data)

    async def put_to_cache(self, data: Data) -> None:
        """Запись данных в БД"""
        await self.redis.set(
            data.phone,
            data.json(),
            ex=BASE_CACHE_EXPIRE_IN_SECONDS,
        )


@lru_cache()
def get_data_service(
    redis: aioredis.Redis = Depends(get_redis),
) -> DataService:
    return DataService(redis)
