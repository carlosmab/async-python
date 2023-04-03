import asyncio

async def say_hello(delay):
    await asyncio.sleep(delay)
    print("Hello, world!")
    

async def main():
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(say_hello(2)))
    await asyncio.gather(*tasks)
    
asyncio.run(main())