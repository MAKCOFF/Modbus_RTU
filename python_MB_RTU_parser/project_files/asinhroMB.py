import asyncio
import traceback
from pymodbus.client.sync import ModbusSerialClient as pyRtu
from _print import _print

# portNbr = "COM4"
# portName = 'com4'
# baud_rate = 9600  # 153600
# parity_E = "E"
# timeoutSp = 0.1

setting_RTU = {
    "method": 'rtu',
    "port": 'COM4',
    "baudrate": 9600,
    "timeout": 0.1,
    "stopbits": 1,
}
arguments_for_write = ([16], 8, 0)
arguments_for_read = ([16], 16, 0)

pymc = pyRtu(setting_RTU)
stop = False


async def read_holding_regs_while(slaves_arr, regs_sp, begin_sp):
    while True:

        await asyncio.sleep(0.5)

        err_cnt = 0

        for slaveId in slaves_arr:

            try:
                value = pymc.read_holding_registers(begin_sp, regs_sp, unit=slaveId)
                t = _print(value)
                print("\r", t, end="")

            except AttributeError:
                err_cnt += 1
                tb = traceback.format_exc()

        if err_cnt > 0:
            print("   !pymodbus:\terrCnt: %s; last tb: %s" % (err_cnt, tb))


async def write_holding_reg(slaves_arr, value, address):
    for k in range(1):

        await asyncio.sleep(1)

        err_cnt = 0

        for slaveId in slaves_arr:

            try:
                data = pymc.write_register(address, value, unit=slaveId)
                # dv = data
                # print("\r", data, end="")
            except AttributeError:
                err_cnt += 1
                tb = traceback.format_exc()

        if err_cnt > 0:
            print("   !pymodbus:\terrCnt: %s; last tb: %s" % (err_cnt, tb))


async def main():
    task1 = asyncio.create_task(read_holding_regs_while(*arguments_for_read))
    task2 = asyncio.create_task(write_holding_reg(*arguments_for_write))

    await asyncio.gather(task1, task2)
    if stop:
        task1.cancel()
        task2.cancel()

# class MBAsyncScraper:


if __name__ == '__main__':
    asyncio.run(main())


