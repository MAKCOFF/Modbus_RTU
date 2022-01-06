"""
Modbus RTU сканер
MODE 1. Сканирует заданные регистры по одному, выводит None если регистра не существует

!!!НЕ сделано!!!
TODO:
   - Выберите режим сканирования
          2. Режим непреывного вывода
          3. Режим записи в регистры:
          3.1 циклической
          3.2 разовой
    - GUI интерфейс!!!
"""
import time
import traceback
from pymodbus.client.sync import ModbusSerialClient as client_RTU
# from project_files.MB_App.MB_App import read_holding_regs_while
import Settings_MB


class MBScraper(client_RTU):
    """
    Для вызова каждой функции класса создается новый объект класса.
    Объекту передаются аргументы, используемые для вызываемой функции
    slaves_arr - список опрашиваемых слэйвов
    regs_sp - число запрашиваемых регистров
    begin_sp - стартовый адрес регистров
    mode_read_registers - 1 HOLDING    ЧТЕНИЕ
                          2 INPUT      ЧТЕНИЕ
                          3 DISCRETE   ЧТЕНИЕ
                          4 COIL       ЧТЕНИЕ
    """
    client = client_RTU(Settings_MB.method, **Settings_MB.setting_RTU)

    # count_obj_of_class = 0
    slaves_arr = [16]  # default value
    regs_sp = 1  # default value
    begin_sp = 0  # default value

    def __init__(self, slaves_arr, regs_sp, begin_sp, mode_read_registers=1):

        # MBScraper.count_obj_of_class += 1
        # print(f"Created obj of MBScraper : {self.count_obj}")
        self.data_result = []
        self.slaves_arr = slaves_arr
        self.regs_sp = regs_sp
        self.begin_sp = begin_sp
        self.tb = None
        self.result = []
        self.mode_read_registers = mode_read_registers
        self.obj_func = None
        self.slave_id_ = None

        super().__init__()

    def __del__(self):
        pass
        # MBScraper.count_obj_of_class -= 1
        # print(f"Вызван деструктор класса, в памяти осталось объектов: {self.count_obj_of_class}")

    @staticmethod
    def time_of_function(function):
        def wrapped(*args):
            start_time = time.perf_counter()
            res = function(*args)
            time_diff = (time.perf_counter() - start_time)
            print("за %.3f sec" % time_diff)
            return res

        return wrapped

    @time_of_function
    def read(self):

        if self.mode_read_registers < 1 or self.mode_read_registers > 4:
            return None, print("Error mode")

        err_cnt = 0
        for slave_id in self.slaves_arr:
            self.slave_id_ = slave_id
            self.data_result.insert(0, self.slave_id_)  # Вставляем в начало списка адрес слэйва int
            for i in range(self.regs_sp):
                match self.mode_read_registers:
                    case 1:  # HOLDING    ЧТЕНИЕ
                        self.obj_func = MBScraper.read_holding_regs(self, i + self.begin_sp, slave_id)
                        if self.obj_func == "None":
                            err_cnt += 1
                        self.data_result.append(self.obj_func)
                    case 2:  # INPUT      ЧТЕНИЕ
                        self.obj_func = MBScraper.read_input_regs(self, i + self.begin_sp, slave_id)
                        if self.obj_func == "None":
                            err_cnt += 1
                        self.data_result.append(self.obj_func)
                    case 3:  # DISCRETE   ЧТЕНИЕ
                        self.obj_func = MBScraper.read_discrete_inputs_regs(self, i + self.begin_sp, slave_id)
                        if self.obj_func == "None":
                            err_cnt += 1
                        self.data_result.append(self.obj_func)
                    case 4:  # COIL       ЧТЕНИЕ
                        self.obj_func = MBScraper.read_coil_regs(self, i + self.begin_sp, slave_id)
                        if self.obj_func == "None":
                            err_cnt += 1
                        self.data_result.append(self.obj_func)
        fact_reg = len(self.data_result) - 1 - err_cnt  # Отнимаем от длины списка индекс адреса слэйва -1
        MBScraper.printing_to_cons(self, fact_reg, err_cnt)

        self.result = [self.data_result, fact_reg, self.tb, err_cnt]
        return self.result

    def printing_to_cons(self, fact_reg, err_cnt):

        match self.mode_read_registers:
            case 1:
                print("Запрошено", len(self.data_result) - 1,
                      "регистров по одному(size 2 BYTE) за каждый запрос \n",
                      "Считано c устройства", self.slave_id_, "HOLDING регистров", fact_reg, "\n",
                      self.data_result)
                if err_cnt > 0:
                    print("   !pymodbus:\terr_cnt: %s; last tb: %s" % (err_cnt, self.tb))
            case 2:
                print("Запрошено", len(self.data_result) - 1,
                      "регистров по одному(size 2 BYTE) за каждый запрос \n",
                      "Считано c устройства", self.slave_id_, "INPUT регистров", fact_reg, "\n", self.data_result)
                if err_cnt > 0:
                    print("   !pymodbus:\terr_cnt: %s; last tb: %s" % (err_cnt, self.tb))
            case 3:
                print("Запрошено", len(self.data_result) - 1,
                      "регистров по одному(size 1 BIT) за каждый запрос \n",
                      "Считано c устройства", self.slave_id_, "DISCRETE INPUT регистров", fact_reg, "\n",
                      self.data_result)
                if err_cnt > 0:
                    print("   !pymodbus:\terrCnt: %s; last tb: %s" % (err_cnt, self.tb))
            case 4:
                print("Запрошено", len(self.data_result) - 1,
                      "регистров по одному(size 1 BIT) за каждый запрос \n",
                      "Считано c устройства", self.slave_id_, "COIL регистров", fact_reg, "\n", self.data_result)
                if err_cnt > 0:
                    print("   !pymodbus:\terrCnt: %s; last tb: %s" % (err_cnt, self.tb))

    def read_holding_regs(self, i, slave_id):
        data = self.client.read_holding_registers(i, 1, unit=slave_id)
        assert (not data.isError())  # test that we are not an error
        if hasattr(data, "registers"):
            meta_data = data.registers
            return "".join(map(str, meta_data))  # Преобразуем из списка в строку
        else:
            self.tb = traceback.format_exc()
            return "None"

    def read_input_regs(self, i, slave_id):
        data = self.client.read_input_registers(i, 1, unit=slave_id)
        assert (not data.isError())  # test that we are not an error
        if hasattr(data, "registers"):
            meta_data = data.registers
            return "".join(map(str, meta_data))
        else:
            self.tb = traceback.format_exc()
            return "None"

    def read_discrete_inputs_regs(self, i, slave_id):
        data_read = []
        data = self.client.read_discrete_inputs(i, 1, unit=slave_id)
        if hasattr(data, "bits"):
            data_read.append(data.bits[0])
            return "".join(map(str, data_read))
        else:
            self.tb = traceback.format_exc()
            return "None"

    def read_coil_regs(self, i, slave_id):
        data_read = []
        data = self.client.read_coils(i, 1, unit=slave_id)
        if hasattr(data, "bits"):
            data_read.append(data.bits[0])
            return "".join(map(str, data_read))
        else:
            self.tb = traceback.format_exc()
            return "None"


if __name__ == '__main__':
    # Селектор режимов
    mode = 1
    match mode:
        case 1:  # Сканирует заданные регистры по одному, выводит None если регистра не существует
            hr = MBScraper(begin_sp=0, regs_sp=20, slaves_arr=[16], mode_read_registers=1).read()
            ir = MBScraper(begin_sp=0, regs_sp=20, slaves_arr=[16], mode_read_registers=2).read()
            dr = MBScraper(begin_sp=0, regs_sp=10, slaves_arr=[16], mode_read_registers=3).read()
            cr = MBScraper(begin_sp=0, regs_sp=10, slaves_arr=[16], mode_read_registers=4).read()
        case 2:  # Непрерывное чтение
            pass
            # read_holding_regs_while([16], 16, 0)

MBScraper.client.close()
