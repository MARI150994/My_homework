import aiohttp
import asyncio
from jsonplaceholder_requests import fetch_users, fetch_posts
from models import User, Post, engine, Session, Base


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(session, users):
    data = []
    for user in users:
        data.append(User(id=user.get('id'),
                         name=user.get('name'),
                         username=user.get('username'),
                         email=user.get('email'),
                         )
                    )
    session.add_all(data)
    await session.commit()


async def create_posts(session, posts):
    data = []
    for post in posts:
        data.append(Post(id=post.get('id'),
                         title=post.get('title'),
                         body=post.get('body'),
                         user_id=post.get('userId'),
                         )
                    )
        session.add_all(data)
    await session.commit()


async def async_main():
    async with aiohttp.ClientSession() as session:
        users, posts = await asyncio.gather(
            fetch_users(session),
            fetch_posts(session)
        )

    await create_database()

    async with Session() as session:
        await create_users(session, users)
        await create_posts(session, posts)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
