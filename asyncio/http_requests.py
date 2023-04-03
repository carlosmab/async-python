import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
    

async def main():
    urls = ["https://www.google.com", "https://www.python.org"]

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.create_task(fetch(session, url)))
        htmls = await asyncio.gather(*tasks)
        for html in htmls:
            print(html[:100])

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())