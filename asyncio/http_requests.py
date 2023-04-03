import asyncio
import requests

async def fetch(url):
    response = await asyncio.to_thread(requests.get, url)
    return response.text[:100]


async def main():
    urls =  ['https://www.google.com', 'https://www.github.com', 'https://www.python.org']
    htmls = await asyncio.gather(*(asyncio.create_task(fetch(url)) for url in urls))
    for html in htmls:
        print(html)
        

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())