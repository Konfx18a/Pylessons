import asyncio


async  def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1,6):
        await asyncio.sleep(40/power)
        print(f'Силач {name} поднял шар номер {i}.')
    print(f"Силач {name} закончил соревнования.")
    return name

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Arnold- mr Olimpia',10))
    task2 = asyncio.create_task(start_strongman('Витя - третьеклассник', 20))
    task3 = asyncio.create_task(start_strongman('Коля - рахит', 40))
    await task1
    await task2
    await task3
    st_man_objs = (start_strongman('Arnold- mr Olimpia',10),
                   start_strongman('Витя - третьеклассник', 20),
                   start_strongman('Коля - рахит', 40))
    rez = await asyncio.gather(*st_man_objs)
    print(f"Соревнования закончены! Победил {rez[-1]} ")

asyncio.run(start_tournament())
