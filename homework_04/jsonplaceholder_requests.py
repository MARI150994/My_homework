import asyncio
import aiohttp
import time


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_users(session):
    async with session.get(USERS_DATA_URL) as response:
        result = await response.json()
        return result

async def fetch_posts(session):
    async with session.get(POSTS_DATA_URL) as response:
        result = await response.json()
        return result
