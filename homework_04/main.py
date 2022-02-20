"""
доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import aiohttp
import asyncio
from jsonplaceholder_requests import fetch_users, fetch_posts


async def async_main():
    async with aiohttp.ClientSession() as session:
        users, posts = await asyncio.gather(
            fetch_users(session),
            fetch_posts(session)
        )
        print(users)
        print(posts)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
