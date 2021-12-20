#!/usr/bin/env python
"""
Pymodbus Asynchronous Client Examples
--------------------------------------------------------------------------

The following is an example of how to use the asynchronous serial modbus
client implementation from pymodbus with ayncio.

The example is only valid on Python3.4 and above
"""
from pymodbus.compat import IS_PYTHON3, PYTHON_VERSION

if IS_PYTHON3 and PYTHON_VERSION >= (3, 4):
    import logging
    import asyncio
    from pymodbus.client.asynchronous.serial import (
        AsyncModbusSerialClient as ModbusClient)
    from pymodbus.client.asynchronous import schedulers
else:
    import sys

    sys.stderr("This example needs to be run only on python 3.4 and above")
    sys.exit(1)

# --------------------------------------------------------------------------- #
# configure the client logging
# --------------------------------------------------------------------------- #
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# --------------------------------------------------------------------------- #
# specify slave to query
# --------------------------------------------------------------------------- #
# The slave to query is specified in an optional parameter for each
# individual request. This can be done by specifying the `unit` parameter
# which defaults to `0x00`
# --------------------------------------------------------------------------- #


UNIT = 0x10  # 0x01


async def start_async_test(client):
    # ----------------------------------------------------------------------- #
    # specify slave to query
    # ----------------------------------------------------------------------- #
    # The slave to query is specified in an optional parameter for each
    # individual request. This can be done by specifying the `unit` parameter
    # which defaults to `0x00`
    # указать ведомое устройство для запроса #
    # ------------------------------------------------- ---------------------- #
    # Подчиненное устройство для запроса указывается в необязательном параметре для каждого
    # индивидуальный запрос. Это можно сделать, указав параметр unit.
    # по умолчанию `0x00`
    # ----------------------------------------------------------------------- #
    try:
        # ----------------------------------------------------------------------- #
        # example requests
        # ----------------------------------------------------------------------- #
        # simply call the methods that you would like to use.
        # An example session is displayed below along with some assert checks.
        # Note that some modbus implementations differentiate holding/
        # input discrete/coils and as such you will not be able to write to
        # these, therefore the starting values are not known to these tests.
        # Furthermore, some use the same memory blocks for the two sets,
        # so a change to one is a change to the other.
        # Keep both of these cases in mind when testing as the following will
        # _only_ pass with the supplied asynchronous modbus server (script supplied).
        # ----------------------------------------------------------------------- #

        # пример запросов
        # ------------------------------------------------- ---------------------- #
        # просто вызовите методы, которые хотите использовать.
        # Ниже показан пример сеанса вместе с некоторыми проверками assert.
        # Обратите внимание, что некоторые реализации Modbus различают удержание
        # ввод дискретных / катушек, поэтому вы не сможете писать на
        # эти, поэтому начальные значения не известны этим тестам.
        # Кроме того, некоторые используют одни и те же блоки памяти для двух наборов,
        # поэтому изменение одного - это изменение другого.
        # Имейте в виду оба этих случая при тестировании, так как следующее будет
        # _только_ пройти с предоставленным асинхронным сервером Modbus (сценарий включен).

        # If the returned output quantity is not a multiple of eight,
        # the remaining bits in the final data byte will be padded with zeros
        # (toward the high order end of the byte).

        # Если возвращаемое количество на выходе не кратно восьми,
        # оставшиеся биты в последнем байте данных будут дополнены нулями
        # (ближе к старшему концу байта).

        # log.debug("Write to a Coil and read back")
        # rq = await client.write_coil(0, True, unit=UNIT)
        # rr = await client.read_coils(0, 1, unit=UNIT)
        # assert (rq.function_code < 0x80)  # test that we are not an error
        # assert (rr.bits[0] == True)  # test the expected value
        #
        # log.debug("Write to multiple coils and read back- test 1")
        # rq = await client.write_coils(1, [True] * 8, unit=UNIT)
        # assert (rq.function_code < 0x80)  # test that we are not an error
        # rr = await client.read_coils(1, 21, unit=UNIT)
        # assert (rr.function_code < 0x80)  # test that we are not an error
        # resp = [True] * 21
        #
        # resp.extend([False] * 3)
        # assert (rr.bits == resp)  # test the expected value

        # log.debug("Write to multiple coils and read back - test 2")
        # rq = await client.write_coils(1, [False] * 8, unit=UNIT)
        # rr = await client.read_coils(1, 8, unit=UNIT)
        # assert (rq.function_code < 0x80)  # test that we are not an error
        # assert (rr.bits == [False] * 8)  # test the expected value
        #
        # log.debug("Read discrete inputs")
        # rr = await client.read_discrete_inputs(0, 8, unit=UNIT)
        # assert (rq.function_code < 0x80)  # test that we are not an error

        log.debug("Write to a holding register and read back")
        rq = await client.write_register(16, 21845, unit=UNIT)
        rr = await client.read_holding_registers(1, 8, unit=UNIT)
        assert (rq.function_code < 0x80)  # test that we are not an error
        assert (rr.registers[0] == 8)  # test the expected value

        # log.debug("Write to multiple holding registers and read back")
        # rq = await client.write_registers(1, [10] * 8, unit=UNIT)
        # rr = await client.read_holding_registers(1, 8, unit=UNIT)
        # assert (rq.function_code < 0x80)  # test that we are not an error
        # assert (rr.registers == [10] * 8)  # test the expected value
        #
        # log.debug("Read input registers")
        # rr = await client.read_input_registers(1, 8, unit=UNIT)
        # assert (rq.function_code < 0x80)  # test that we are not an error
        #
        # arguments = {
        #     'read_address': 1,
        #     'read_count': 8,
        #     'write_address': 1,
        #     'write_registers': [20] * 8,
        # }
        # log.debug("Read write registers simulataneously")
        # rq = await client.readwrite_registers(unit=UNIT, **arguments)
        # rr = await client.read_holding_registers(1, 8, unit=UNIT)
        # assert (rq.function_code < 0x80)  # test that we are not an error
        # assert (rq.registers == [20] * 8)  # test the expected value
        # assert (rr.registers == [20] * 8)  # test the expected value
    except Exception as e:
        log.exception(e)
        client.transport.close()
    await asyncio.sleep(1)


if __name__ == '__main__':
    # ----------------------------------------------------------------------- #
    # For testing on linux based systems you can use socat to create serial
    # ports
    # ----------------------------------------------------------------------- #
    # socat -d -d PTY,link=/tmp/ptyp0,raw,echo=0,ispeed=9600 PTY,
    # link=/tmp/ttyp0,raw,echo=0,ospeed=9600

    loop, client = ModbusClient(schedulers.ASYNC_IO,
                                port='COM4',
                                baudrate=9600,
                                method="rtu",
                                parity="E",
                                )

    loop.run_until_complete(start_async_test(client.protocol))

    loop.close()
