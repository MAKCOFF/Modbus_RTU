import traceback
from collections import namedtuple
from pymodbus.client.sync import ModbusSerialClient as pyRtu

'''
portNbr = "COM4"
portName = 'com4'
baudrate = 9600  
parity_E = "E"
'''
timeoutSp = 0.1  # 0.018 + regsSp*0

RTUSettings = namedtuple('RTU_Settings', ['method', 'port', 'baudrate', 'timeout', 'parity', 'stopbits'])
unit = RTUSettings('rtu', 'COM4', 9600, timeoutSp, 'E', 1)
print(unit)

print("timeout: %s [s]" % timeoutSp)

# pymc = pyRtu(method='rtu', port=portNbr, baudrate=baudrate, timeout=timeoutSp, parity=parity_E, stopbits=1)
print(unit._asdict())
pymc = pyRtu(**unit._asdict())


def write_holding_reg(
        slaves_arr,
        value,
        address
):
    errCnt = 0

    for slaveId in slaves_arr:

        try:
            data = pymc.write_register(address, value, unit=slaveId)

        except AttributeError:
            errCnt += 1
            tb = traceback.format_exc()

    print("\r", data, end="")

    if errCnt > 0:
        print("   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))

    # print("\r", data, data.registers, end="")
    # print("pymodbus:\t time to read %s x %s (x %s regs): %.3f [s] / %.3f [s/req]" % (
    # len(slavesArr), iterSp, regsSp, timeDiff, timeDiff / iterSp))

write_holding_reg([16], 8, 0)