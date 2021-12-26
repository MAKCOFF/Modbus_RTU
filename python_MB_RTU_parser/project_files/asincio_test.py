import asyncio


async def gen():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.2)


async def gen_2():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} second have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(gen())
    task2 = asyncio.create_task(gen_2())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())
