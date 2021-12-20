import time
import traceback
from pymodbus.client.sync import ModbusSerialClient as pyRtu
from MB_while import read_holding_regs_while
# import asyncio

mode = 2
scan = True
portNbr = "COM4"
portName = 'com4'
baudrate = 9600  # 153600
parity_E = "E"
timeoutSp = 0.1  # 0.018 + regsSp*0
print("timeout: %s [s]" % timeoutSp)

pymc = pyRtu(method='rtu', port=portNbr, baudrate=baudrate, timeout=timeoutSp, parity=parity_E, stopbits=1)


def read_holding_regs(
        slavesArr,
        regsSp,
        beginSp
):
    errCnt = 0
    startTs = time.time()

    data_read = []

    for slaveId in slavesArr:

        for p in range(beginSp, regsSp):

            try:
                data = pymc.read_holding_registers(p, 1, unit=slaveId)
                data_read.append(data.registers)
            except AttributeError:
                errCnt += 1
                tb = traceback.format_exc()
                data_read.append(str("None"))

    stopTs = time.time()
    timeDiff = stopTs - startTs
    fact_reg = len(data_read) - errCnt

    print("Запрошено", len(data_read),
          "регистров по одному(size 2 BYTE) за каждый запрос \n",
          "Считано c устройства", slaveId, "HOLDING регистров", fact_reg, "\n", data_read, "\n",
          "за %.3f sec" % timeDiff)

    if errCnt > 0:
        print("   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))

    # print("\r", data, data.registers, end="")
    # print("pymodbus:\t time to read %s x %s (x %s regs): %.3f [s] / %.3f [s/req]" % (
    # len(slavesArr), iterSp, regsSp, timeDiff, timeDiff / iterSp))


async def read_input_regs(
        slavesArr,
        regsSp,
        beginSp
):
    errCnt = 0
    startTs = time.time()

    data_read = []

    for slaveId in slavesArr:

        for p in range(beginSp, regsSp):

            try:
                data = pymc.read_input_registers(p, 1, unit=slaveId)
                data_read.append(data.registers)
            except AttributeError:
                errCnt += 1
                tb = traceback.format_exc()
                data_read.append(str("None"))

    stopTs = time.time()
    timeDiff = stopTs - startTs
    fact_reg = len(data_read) - errCnt

    print("Запрошено", len(data_read),
          "регистров по одному(size 1 BIT) за каждый запрос \n",
          "Считано c устройства", slaveId, "INPUT регистров", fact_reg, "\n", data_read, "\n",
          "за %.3f sec" % timeDiff)

    if errCnt > 0:
        print("   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))

    # print("\r", data, data.registers, end="")
    # print("pymodbus:\t time to read %s x %s (x %s regs): %.3f [s] / %.3f [s/req]" % (
    # len(slavesArr), iterSp, regsSp, timeDiff, timeDiff / iterSp))


async def read_discret_inputs(
        slavesArr,
        regsSp,
        beginSp
):
    errCnt = 0
    startTs = time.time()

    data_read = []

    for slaveId in slavesArr:

        for p in range(beginSp, regsSp):

            try:
                data = pymc.read_discrete_inputs(p, 1, unit=slaveId)
                data_read.append(data.bits)
            except AttributeError:
                errCnt += 1
                tb = traceback.format_exc()
                data_read.append(str("None"))

    stopTs = time.time()
    timeDiff = stopTs - startTs
    fact_reg = len(data_read) - errCnt

    data_byte_to_bit = []

    for j in range(len(data_read)):
        el = data_read[j]
        if el == str('None'):
            data_byte_to_bit.append("None")
        elif 8 == len(el):
            data_byte_to_bit.append([el[0]])

    print("Запрошено", len(data_read),
          "регистров по одному(size 1 BIT) за каждый запрос \n",
          "Считано c устройства", slaveId, "DISCRET INPUT регистров", fact_reg, "\n", data_byte_to_bit, "\n",
          "за %.3f sec" % timeDiff)

    if errCnt > 0:
        print("   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))

    # print("\r", data, data.registers, end="")
    # print("pymodbus:\t time to read %s x %s (x %s regs): %.3f [s] / %.3f [s/req]" % (
    # len(slavesArr), iterSp, regsSp, timeDiff, timeDiff / iterSp))


async def read_coil_regs(
        slavesArr,
        regsSp,
        beginSp
):
    errCnt = 0
    startTs = time.time()

    data_read = []

    for slaveId in slavesArr:

        for p in range(beginSp, regsSp):

            try:
                data = pymc.read_coils(p, 1, unit=slaveId)
                data_read.append(data.bits)
            except AttributeError:
                errCnt += 1
                tb = traceback.format_exc()
                data_read.append(str("None"))

    stopTs = time.time()
    timeDiff = stopTs - startTs
    fact_reg = len(data_read) - errCnt

    data_byte_to_bit = []

    for l in range(len(data_read)):
        el = data_read[l]
        if el == str("None"):
            data_byte_to_bit.append("None")
        elif 8 == len(el):
            data_byte_to_bit.append([el[0]])

    print("Запрошено", len(data_read),
          "регистров по одному(size 1 BIT) за каждый запрос \n",
          "Считано c устройства", slaveId, "COIL регистров", fact_reg, "\n", data_byte_to_bit, "\n",
          "за %.3f sec" % timeDiff)

    if errCnt > 0:
        print("   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))

    # print("\r", data, data.registers, end="")
    # print("pymodbus:\t time to read %s x %s (x %s regs): %.3f [s] / %.3f [s/req]" % (
    # len(slavesArr), iterSp, regsSp, timeDiff, timeDiff / iterSp))


# Селектор режимов

if mode == 1:

    # Сканирует заданные регистры по одному, выводит None если регистра не существует

    for j in range(1):
        read_holding_regs([16], 16, 0)
        # read_input_regs([16], 11, 0)
        # read_discret_inputs([16], 23, 0)
        # read_coil_regs([16], 5, 0)
        # pymc.close()

elif mode == 2:

        read_holding_regs_while([16], 16, 0)

# elif mode == 3:
#
#
# else:
#     print("Выберите режим сканирования\n"
#           "1. Режим парсинга регистров\n"
#           "2. Режим Непреывного вывода в консоль значений\n"
#           "3. Режим записи в регистры: \n"
#           "3.1 циклической\n"
#           "3.2 разовой\n")
pymc.close()
