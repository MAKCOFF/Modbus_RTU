import traceback
from collections import namedtuple
from pymodbus.client.sync import ModbusSerialClient as pyRtu
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian

'''
portNbr = "COM1"  # for Linux /dev/ttyS1
portName = 'com1'  # for Linux /dev/ttyS1
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
    address = 0
    values = [20, 40, 60, 80, 100]

    builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Big)
    builder.add_32bit_float(-20.85)
    builder.add_32bit_float(5.85)
    payload = builder.build()
    print(payload)
    # v = b'\xa6A'
    # t = int.from_bytes(v, byteorder='little')
    # print(t)
    # decoder = BinaryPayloadDecoder(payload, byteorder=Endian.Little)
    # value_1 = decoder.decode_32bit_float()
    # value_2 = decoder.decode_32bit_float()
    # # print("".join(value))
    # assert decoder._byteorder == builder._byteorder
    # decoded = OrderedDict([
    #     ('string', decoder.decode_string(len(strng))),
    #     ('bits', decoder.decode_bits()),
    #     ('8int', decoder.decode_8bit_int()),
    #     ('8uint', decoder.decode_8bit_uint()),
    #     ('16int', decoder.decode_16bit_int()),
    #     ('16uint', decoder.decode_16bit_uint()),
    #     ('32int', decoder.decode_32bit_int()),
    #     ('32uint', decoder.decode_32bit_uint()),
    #     ('16float', decoder.decode_16bit_float()),
    #     ('16float2', decoder.decode_16bit_float()),
    #     ('32float', decoder.decode_32bit_float()),
    #     ('32float2', decoder.decode_32bit_float()),
    #     ('64int', decoder.decode_64bit_int()),
    #     ('64uint', decoder.decode_64bit_uint()),
    #     ('ignore', decoder.skip_bytes(8)),
    #     ('64float', decoder.decode_64bit_float()),
    #     ('64float2', decoder.decode_64bit_float()),
    # ])

    try:
        data_write = pymc.write_registers(address=address, values=payload, unit=16, skip_encode=True)
        data_read = pymc.read_holding_registers(address=address, count=8, unit=16)
        decoder = BinaryPayloadDecoder.fromRegisters(data_read.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        value_1 = decoder.decode_32bit_float()
        value_2 = decoder.decode_32bit_float()
        arr = [value_1, value_2]
        print(data_write, "\n", arr)
    except AttributeError:
        errCnt += 1
        tb = traceback.format_exc()

    if errCnt > 0:
        print("   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))


if __name__ == '__main__':

    write_holding_reg()
