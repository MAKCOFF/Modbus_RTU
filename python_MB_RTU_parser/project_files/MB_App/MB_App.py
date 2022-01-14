"""
Modbus RTU сканер
MODE 1. Сканирует заданные регистры по одному, выводит строку "None" если регистра не существует

!!!НЕ сделано!!!
TODO:
   - Выберите режим сканирования
          2. Режим непреывного чтения - не отлажен
          3. Режим записи в регистры:
          3.1 циклической
          3.2 разовой
    - GUI интерфейс!!!
"""
import traceback
from pymodbus.client.sync import ModbusSerialClient as client_RTU
import Settings_MB
import App_modules
from time import sleep


class MBScraper(client_RTU):
    """
    Для вызова каждой функции класса создается новый объект класса.
    Объекту передаются аргументы, используемые для вызываемой функции
    slaves_arr - список опрашиваемых слэйвов
    quantity_registers - число запрашиваемых регистров
    number_first_register - стартовый адрес регистров
    mode_read_registers - 1 HOLDING    ЧТЕНИЕ
                          2 INPUT      ЧТЕНИЕ
                          3 DISCRETE   ЧТЕНИЕ
                          4 COIL       ЧТЕНИЕ
    """
    client = client_RTU(Settings_MB.method, **Settings_MB.setting_RTU)

    slaves_arr = [16]  # default value
    number_first_register_read = 0  # default value
    quantity_registers_read = 10  # default value
    number_first_register_write = 11  # default value
    values_for_write_registers = [80, 50, 25, 10]
    start = False
    stop = False

    # count_obj_of_class = 0  # debug

    def __init__(self, slaves_arr, quantity_registers_read, number_first_register_read):

        # self.count_obj_of_class += 1  # debug
        # print(f"Created obj of MBScraper : {self.count_obj}")  # debug
        self.data_result = []
        self.slaves_arr = slaves_arr
        self.quantity_registers_read = quantity_registers_read
        self.number_first_register_read = number_first_register_read
        self.traceback_error = None
        self.result = []
        self.mode_read_registers = 1
        self.result_of_reading = None
        self.slave_id_ = None
        self.error_count = 0
        self.fact_reg = 0

        super().__init__()

    def __del__(self):
        self.client.close()
        # self.count_obj_of_class -= 1  # debug
        # print(f"Вызван деструктор класса, в памяти осталось объектов: {self.count_obj_of_class}")  # debug

    @App_modules.time_of_function
    def read_init(self, mode_read_registers=1):
        self.error_count = 0
        for slave_id in self.slaves_arr:
            self.slave_id_ = slave_id
            self.data_result.insert(0, self.slave_id_)  # Вставляем в начало списка адрес слэйва int
            for register in range(self.quantity_registers_read):
                match mode_read_registers:
                    case 1:  # HOLDING    ЧТЕНИЕ
                        self.result_of_reading = \
                            self.read_holding_regs(register + self.number_first_register_read, slave_id)
                        if self.result_of_reading == "None":
                            self.error_count += 1
                        self.data_result.append(self.result_of_reading)
                    case 2:  # INPUT      ЧТЕНИЕ
                        self.result_of_reading = \
                            self.read_input_regs(register + self.number_first_register_read, slave_id)
                        if self.result_of_reading == "None":
                            self.error_count += 1
                        self.data_result.append(self.result_of_reading)
                    case 3:  # DISCRETE   ЧТЕНИЕ
                        self.result_of_reading =\
                            self.read_discrete_inputs_regs(register + self.number_first_register_read, slave_id)
                        if self.result_of_reading == "None":
                            self.error_count += 1
                        self.data_result.append(self.result_of_reading)
                    case 4:  # COIL       ЧТЕНИЕ
                        self.result_of_reading = \
                            self.read_coil_regs(register + self.number_first_register_read, slave_id)
                        if self.result_of_reading == "None":
                            self.error_count += 1
                        self.data_result.append(self.result_of_reading)
                    case _:
                        return

        self.fact_reg = len(self.data_result) - 1 - self.error_count  # Отнимаем от длины списка индекс адреса слэйва -1

        App_modules.printing_to_console(self, mode_read_registers)

        self.result = [self.data_result, self.fact_reg, self.traceback_error, self.error_count]
        return self.result

    def read_holding_regs(self, register, slave_id):
        data = self.client.read_holding_registers(register, 1, unit=slave_id)
        assert (not data.isError())
        if hasattr(data, "registers"):
            meta_data = data.registers
            return "".join(map(str, meta_data))  # Преобразуем из списка в строку
        else:
            self.traceback_error = traceback.format_exc()
            return "None"

    def read_input_regs(self, register, slave_id):
        data = self.client.read_input_registers(register, 1, unit=slave_id)
        assert (not data.isError())
        if hasattr(data, "registers"):
            meta_data = data.registers
            return "".join(map(str, meta_data))
        else:
            self.traceback_error = traceback.format_exc()
            return "None"

    def read_discrete_inputs_regs(self, register, slave_id):
        data_read = []
        data = self.client.read_discrete_inputs(register, 1, unit=slave_id)
        assert (not data.isError())
        if hasattr(data, "bits"):
            data_read.append(data.bits[0])
            return "".join(map(str, data_read))
        else:
            self.traceback_error = traceback.format_exc()
            return "None"

    def read_coil_regs(self, register, slave_id):
        data_read = []
        data = self.client.read_coils(register, 1, unit=slave_id)
        assert (not data.isError())
        if hasattr(data, "bits"):
            data_read.append(data.bits[0])
            return "".join(map(str, data_read))
        else:
            self.traceback_error = traceback.format_exc()
            return "None"

    def read_write_regs(self, slave_id):
        while self.start:
            if self.stop:
                break
            data = self.client.readwrite_registers(self.number_first_register_read, self.quantity_registers_read,
                                                   self.number_first_register_write, self.values_for_write_registers,
                                                   unit=slave_id)
            assert (not data.isError())
            if hasattr(data, "registers"):
                meta_data = data.registers
                return "".join(map(str, meta_data))  # Преобразуем из списка в строку
            else:
                self.traceback_error = traceback.format_exc()
                return "None"


if __name__ == '__main__':
    # Селектор режимов
    mode_read = 1
    match mode_read:
        case 1:  # Сканирует заданные регистры по одному, выводит строку "None" если регистра не существует
            hr = MBScraper(number_first_register_read=0, quantity_registers_read=20, slaves_arr=[16]).read_init(1)
            ir = MBScraper(number_first_register_read=0, quantity_registers_read=20, slaves_arr=[16]).read_init(2)
            dr = MBScraper(number_first_register_read=0, quantity_registers_read=10, slaves_arr=[16]).read_init(3)
            cr = MBScraper(number_first_register_read=0, quantity_registers_read=10, slaves_arr=[16]).read_init(4)
        case 2:  # Непрерывное чтение
            while MBScraper.start:
                if MBScraper.stop:
                    break
                sleep(0.5)
                h = App_modules.read_holding_w(MBScraper, 0, 20, 16)
                sleep(0.2)
                i = App_modules.read_input_w(MBScraper, 0, 20, 16)
                sleep(0.2)
                d = App_modules.read_discrete_inputs_w(MBScraper, 0, 10, 16)
                sleep(0.2)
                c = App_modules.read_coil_w(MBScraper, 0, 10, 16)
                print(h, "\n", i, "\n", d, "\n", c)
        case 3:  # Циклическая запись и чтение одновременно
            hr = MBScraper(number_first_register_read=0, quantity_registers_read=20,
                           slaves_arr=[16]).read_write_regs(16)
