import asyncio

async def hello():
    # print("Hello, world!")
    return "Result from hello"
async def main():
    await hello()
    print(await hello())
    
asyncio.run(main())