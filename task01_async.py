import asyncio
import aiohttp
import time

# список url
urls = ['https://www.example.com'] * 10


async def fetch_url_async(session, url):
    async with session.get(url) as response:
        await response.text()  # Получение тела ответа
        return response.status


async def fetch_all_urls():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url_async(session, url) for url in urls]
        await asyncio.gather(*tasks)


def asyncio_method():
    start_time = time.time()
    asyncio.run(fetch_all_urls())
    end_time = time.time()
    print(f'asyncio time: {end_time - start_time: 0.2f} seconds\n')


if __name__ == '__main__':
    print("Running with asyncio:")
    asyncio_method()
