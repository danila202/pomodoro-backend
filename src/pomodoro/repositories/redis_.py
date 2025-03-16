import abc
import json

import redis.asyncio as redis

class AbstractRedisClient(abc.ABC):

    @abc.abstractmethod
    async def set_key(self, key: str, value: dict):
        raise NotImplementedError
    
    @abc.abstractmethod
    async def fetch_key(self, key: str) -> dict:
        raise NotImplementedError


class RedisClient:
    def __init__(self, redis_client: redis.Redis):
        self.redis_client = redis_client
    
    async def set_key(self, key: str, value: dict):
        await self.redis_client.set(key, json.dumps(value))
    
    async def fetch_key(self, key: str) -> dict:
        data = await self.redis_client.get(key)
        return json.loads(data)
