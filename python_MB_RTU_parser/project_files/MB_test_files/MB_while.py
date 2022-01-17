import traceback
from pymodbus.client.sync import ModbusSerialClient as pyRtu
from time import sleep

portNbr = "COM1"
portName = 'com1'
baudrate = 9600  # 153600
parity_E = "E"
timeoutSp = 0.1

pymc = pyRtu(method='rtu', port=portNbr, baudrate=baudrate, timeout=timeoutSp, parity=parity_E, stopbits=1)


def read_holding_regs_while(
        slavesArr,
        regsSp,
        beginSp
):
    while True:

        sleep(0.5)

        errCnt = 0

        for slaveId in slavesArr:

            try:
                data = pymc.read_holding_registers(beginSp, regsSp, unit=slaveId)

            except AttributeError:
                errCnt += 1
                tb = traceback.format_exc()

        print("\r", data, data.registers, end="")

        if errCnt > 0:
            print("   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))


def read_input_regs_while(
        slavesArr,
        regsSp,
        beginSp
):
    errCnt = 0

    for slaveId in slavesArr:

        try:
            data = pymc.read_input_registers(beginSp, regsSp, unit=slaveId)
        except AttributeError:
            errCnt += 1
            tb = traceback.format_exc()

    print("\r", data, data.registers, end="")

    if errCnt > 0:
        print("   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))


def read_discret_inputs_while(
        slavesArr,
        regsSp,
        beginSp
):
    errCnt = 0

    for slaveId in slavesArr:

        try:
            data = pymc.read_discrete_inputs(beginSp, regsSp, unit=slaveId)
        except AttributeError:
            errCnt += 1
            tb = traceback.format_exc()

    print("\r", data, data.bits, end="")

    if errCnt > 0:
        print("   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))


def read_coil_regs_while(
        slavesArr,
        regsSp,
        beginSp
):
    errCnt = 0

    for slaveId in slavesArr:

        try:
            data = pymc.read_coils(beginSp, regsSp, unit=slaveId)
        except AttributeError:
            errCnt += 1
            tb = traceback.format_exc()

    print("\r", data, data.bits, end="")

    if errCnt > 0:
        print("   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))


if __name__ == '__main__':
    read_holding_regs_while([16], 2, 25)
