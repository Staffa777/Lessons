import asyncio

# from PIL.ImImagePlugin import number


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        number = i+1
        await asyncio.sleep(i*5/power)
        print(f'Силач {name} поднял {number}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    time_1 = asyncio.create_task(start_strongman('Pasha', 3))
    time_2 = asyncio.create_task(start_strongman('Denis', 4))
    time_3 = asyncio.create_task(start_strongman('Apollon', 5))

    await time_1
    await time_2
    await time_3
asyncio.run(start_tournament())
