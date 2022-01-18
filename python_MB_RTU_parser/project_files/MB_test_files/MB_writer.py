import traceback
from collections import namedtuple
from pymodbus.client.sync import ModbusSerialClient as pyRtu

'''
portNbr = "COM1"
portName = 'com1'
baudrate = 9600  
parity_E = "E"
'''
timeoutSp = 0.1  # 0.018 + regsSp*0

RTUSettings = namedtuple('RTU_Settings', ['method', 'port', 'baudrate', 'timeout', 'parity', 'stopbits'])
unit = RTUSettings('rtu', 'COM1', 9600, timeoutSp, 'E', 1)
# print(unit._asdict())
pymc = pyRtu(**unit._asdict())


def write_holding_reg():
    errCnt = 0
    address = 1
    values = [20]

    try:
        data_write = pymc.write_registers(address=address, values=values, unit=16)
        # data_read = pymc.read_holding_registers(address=address, count=4, unit=16)

    except AttributeError:
        errCnt += 1
        tb = traceback.format_exc()

    print(data_write, "\n")  #data_read.registers)

    if errCnt > 0:
        print("   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))


if __name__ == '__main__':

    write_holding_reg()
