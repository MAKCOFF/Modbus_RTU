"""
Modbus RTU сканер
MODE 1. Сканирует заданные регистры по одному, выводит None если регистра не существует

!!!Не сделано ООП, не проверено!!!
"""
import time
import traceback
from pymodbus.client.sync import ModbusSerialClient  # as pyRtu
from MB_while import read_holding_regs_while
import Settings_MB

mode = 1
scan = True


# portNbr = "COM4"
# portName = 'com4'
# baudrate = 9600  # 153600
# parity_E = "E"
# timeoutSp = 0.1  # 0.018 + regsSp*0
# print("timeout: %s [s]" % timeoutSp)

class MBScraper(ModbusSerialClient):
    count_obj = 0
    client = ModbusSerialClient(Settings_MB.setting_RTU)
    slaves_arr = Settings_MB.slaves_arr    # default value
    regs_sp = Settings_MB.regs_sp          # default value
    begin_sp = Settings_MB.begin_sp        # default value

    def __init__(self, slaves_arr, regs_sp, begin_sp):
        MBScraper.count_obj += 1
        print("Created obj of MBScraper - ", self.count_obj)
        self.data_result = []
        self.slaves_arr = slaves_arr
        self.regs_sp = regs_sp
        self.begin_sp = begin_sp
        self.tb = None
        self.result = []

        ModbusSerialClient.__init__(self)

    def read_holding_regs(self):
        err_cnt = 0
        start_ts = time.time()
        for slaveId in self.slaves_arr:
            for i in range(self.begin_sp, self.regs_sp):
                try:
                    data = MBScraper.client.read_holding_registers(i, 1, unit=slaveId)
                    self.data_result.append(data.registers)
                except AttributeError:
                    err_cnt += 1
                    self.tb = traceback.format_exc()
                    self.data_result.append(str("None"))
        stop_ts = time.time()
        time_diff = stop_ts - start_ts
        fact_reg = len(self.data_result) - err_cnt

        print("Запрошено", len(self.data_result),
              "регистров по одному(size 2 BYTE) за каждый запрос \n",
              "Считано c устройства", slaveId, "HOLDING регистров", fact_reg, "\n", self.data_result, "\n",
              "за %.3f sec" % time_diff)

        if err_cnt > 0:
            print("   !pymodbus:\terr_cnt: %s; last tb: %s" % (err_cnt, self.tb))
        # print("\r", data, data.registers, end="")
        # print("pymodbus:\t time to read %s x %s (x %s regs): %.3f [s] / %.3f [s/req]" % (
        # len(slavesArr), iterSp, regsSp, time_diff, time_diff / iterSp))

        self.result = [slaveId, self.data_result, fact_reg, time_diff, self.tb, err_cnt]

        return self.result

    def read_input_regs(self,
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
                    data = MBScraper.client.read_input_registers(p, 1, unit=slaveId)
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

    def mbs_read_discrete_inputs(self,
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
                    data = MBScraper.client.read_discrete_inputs(p, 1, unit=slaveId)
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

    def read_coil_regs(self,
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
                    data = MBScraper.client.read_coils(p, 1, unit=slaveId)
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
if __name__ == '__main__':

    if mode == 1:
        # Сканирует заданные регистры по одному, выводит None если регистра не существует
        hr = MBScraper(begin_sp=0, regs_sp=1, slaves_arr=[16])
        for j in range(1):
            MBScraper.read_holding_regs(hr)
            # MBScraper.read_input_regs(exemp_1, [16], 11, 0)
            # MBScraper.read_discrete_inputs(exemp_1, [16], 23, 0)
            # MBScraper.read_coil_regs(exemp_1, [16], 5, 0)
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
MBScraper.client.close()
