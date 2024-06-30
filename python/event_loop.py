import asyncio

async def kitchen():
    print("Открываем холодильник")
    await asyncio.sleep(0)
    print("Закрываем холодильник")

async def fridge():
    print('Достаём еду')
    await asyncio.sleep(0)
    print('холодильник закрыт')

ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(kitchen()), ioloop.create_task(fridge())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()
