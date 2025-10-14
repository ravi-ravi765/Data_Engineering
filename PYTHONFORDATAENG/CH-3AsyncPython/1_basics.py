import asyncio

# async def process1():

#     print('process-1 first step')
#     await asyncio.sleep(6)
#     print('process -2 second step')

# async def process2():

#     print('process-2 first step')
#     await asyncio.sleep(6)
#     print('process-2 second step')

# # event1 loop begins
# asyncio.run(process1())

# # event3 loop begins
# asyncio.run(process2())

async def process1():

    print('process - 1 first step')
    await asyncio.sleep(6) # there can be an api call
    result  = await process2()
    print(result)
    print('process -1 second step')

async def process2():
    print('process-2 first step')
    await asyncio.sleep(5)
    print('process-2 second step')
    return 'process2 completed..'

# event1 loop begins
asyncio.run(process1())
