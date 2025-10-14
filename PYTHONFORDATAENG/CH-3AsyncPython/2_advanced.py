import asyncio

async def process1():
    print('process-1 first step..')
    await asyncio.sleep(3)
    print('process-1 second step')

async def process2():
    print('process-2 first step')
    await asyncio.sleep(6)
    print('process-2 second step')

async def main():

    tasks = await asyncio.gather(process1(),process2())

    print('main completed')

if __name__ == '__main__':

    asyncio.run(main())
