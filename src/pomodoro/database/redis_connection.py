from contextlib import asynccontextmanager


import redis.asyncio as redis

from src.pomodoro.settings import settings
from src.pomodoro.repositories.redis_ import RedisClient


@asynccontextmanager
async def make_redis_connection():
    pool = redis.ConnectionPool.from_url(settings.redis_uri, max_connections = 10)
    redis_client = redis.Redis(connection_pool=pool)
    try:
        yield redis_client   
    finally:
        await redis_client.aclose()


async def make_redis_client():
    async with make_redis_connection() as redis_client:
        yield RedisClient(redis_client=redis_client)
