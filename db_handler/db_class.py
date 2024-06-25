from os import name
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from decouple import config

class PostgresHandler:
    def __init__(self, pg_link: str):
        self.pg_link = pg_link
        self.pool: Pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(self.pg_link)

    async def close(self):
        await self.pool.close()

    async def execute(self, query: str, *args):
        async with self.pool.acquire() as conn:
            return await conn.execute(query, *args)

    async def fetch(self, query: str, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def fetchrow(self, query: str, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, *args)

    async def fetchval(self, query: str, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetchval(query, *args)

# Пример использования класса PostgresHandler
if __name__ == "__main__":
    pg_link = config('PG_LINK')
    pg_db = PostgresHandler(pg_link)