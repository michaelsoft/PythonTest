import asyncio

async def main():
    print("Hello World")
    await asyncio.sleep(1)
    print("End")

asyncio.run(main())