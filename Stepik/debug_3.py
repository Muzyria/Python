import aiohttp
import asyncio
import time


async def one():
    print("start ONE")
    await asyncio.sleep(5)
    print("stop ONE")

async def two():
    print("start TWO")
    await asyncio.sleep(3)
    print("stop TWO")

async def three():
    print("start THREE")
    await asyncio.sleep(4)
    print("stop THREE")

async def four():
    print("start FOUR")
    await asyncio.sleep(5)
    print("stop FOUR")


async def fetch_url():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://demoqa.com/auto-complete") as response:
            print(f"Status: {response.status}")


async def main():
    # await asyncio.create_task(one())
    # await asyncio.create_task(two())
    # await asyncio.create_task(three())
    # await asyncio.create_task(four())
    # await  asyncio.gather(one(), two(), three(), four())
    # await asyncio.create_task(fetch_url())
    await asyncio.gather(*(fetch_url() for _ in range(5)))


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)

