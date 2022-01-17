import asyncio


def callback(result):
    print("Result = ", result.result())
    event_loop.stop()


async def long_running_func():
    print("long running func started")
    await asyncio.sleep(2)
    return "Completed"


async def main():
    event_loop.create_task(long_running_func()).add_done_callback(callback)
    print("Main completed")


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(main())
event_loop.run_forever()
