#!/home/max/Загрузки/Python-3.10.2/python
#-*- coding: utf-8 -*-
__version__ = 'v 1.0'
"""
Modbus RTU сканер - консольный, только int значения 2 байта
MODE 1. Сканирует заданные регистры по одному, выводит строку "None" если регистра не существует
MODE 2. Непрерывное чтение
MODE 3. Циклическая запись и чтение одним запросом
MODE 4. Одного регистра
"""
import traceback
from pymodbus.client.sync import ModbusSerialClient as client_RTU
import Settings_MB
import App_modules
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import DB_module


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

    number_first_register_write = 0  # default value
    # count_obj_of_class = 0  # debug

    def __init__(self, **kwargs):

        # self.count_obj_of_class += 1  # debug
        # print(f"Created obj of MBScraper : {self.count_obj}")  # debug
        self.data_result = []
        self.slaves_arr = kwargs.get('slaves_arr', [16])
        self.quantity_registers_read = kwargs.get('quantity_registers_read', 5)
        self.number_first_register_read = kwargs.get('number_first_register_read', 0)
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
    def _read_init(self, mode_read_registers=1):
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
                        self.result_of_reading = \
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
        """
        :param register: Текущий регистр для опроса
        :param slave_id: Адрес слэйва
        :return: Возвращает str значение регистра или None при ошибке чтения
        """
        data = self.client.read_holding_registers(register, 1, unit=slave_id)
        assert (not data.isError())
        if hasattr(data, "registers"):
            meta_data = data.registers
            return "".join(map(str, meta_data))  # Преобразуем из списка в строку
        else:
            self.traceback_error = traceback.format_exc()
            return "None"

    def read_input_regs(self, register, slave_id):
        """
        :param register: Текущий регистр для опроса
        :param slave_id: Адрес слэйва
        :return: Возвращает str значение регистра или None при ошибке чтения
        """
        data = self.client.read_input_registers(register, 1, unit=slave_id)
        assert (not data.isError())
        if hasattr(data, "registers"):
            meta_data = data.registers
            return "".join(map(str, meta_data))
        else:
            self.traceback_error = traceback.format_exc()
            return "None"

    def read_discrete_inputs_regs(self, register, slave_id):
        """
        :param register: Текущий регистр для опроса
        :param slave_id: Адрес слэйва
        :return: Возвращает str значение регистра или None при ошибке чтения
        """
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
        """
        :param register: Текущий регистр для опроса
        :param slave_id: Адрес слэйва
        :return: Возвращает str значение регистра или None при ошибке чтения
        """
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
        while True:
            stop = DB_module.get_stop_from_db()
            if stop == 0:
                break
            values = DB_module.get_values_from_db(count=4)
            sleep(0.5)
            data = self.client.readwrite_registers(read_address=self.number_first_register_read,
                                                   read_count=self.quantity_registers_read,
                                                   write_address=self.number_first_register_write,
                                                   write_registers=values,  # self.values_for_write_registers,
                                                   unit=slave_id)
            if hasattr(data, "registers"):
                print(data.registers)
            else:
                self.traceback_error = traceback.format_exc()
                print(self.traceback_error)

    def write_regs(self, address=11, values=50, slave_id=16):
        data = self.client.write_registers(address, values, unit=slave_id)
        print(data)

    def run(self):
        # Селектор режимов
        mode_read = 1
        match mode_read:
            case 1:  # Сканирует заданные регистры по одному, выводит строку "None" если регистра не существует
                MBScraper()._read_init(1)
                MBScraper()._read_init(2)
                MBScraper()._read_init(3)
                MBScraper()._read_init(4)
            case 2:  # Непрерывное чтение
                while True:
                    stop = DB_module.get_stop_from_db()
                    if stop == 0:
                        break
                    sleep(0.3)
                    App_modules.read_holding_w(MBScraper, 0, 20, 16)
                    sleep(0.3)
                    App_modules.read_input_w(MBScraper, 0, 20, 16)
                    sleep(0.3)
                    App_modules.read_discrete_inputs_w(MBScraper, 0, 10, 16)
                    sleep(0.3)
                    App_modules.read_coil_w(MBScraper, 0, 10, 16)
            case 3:  # Циклическая запись и чтение одновременно
                self.read_write_regs(16)
            case 4:  # Разовая запись
                self.write_regs()


if __name__ == '__main__':
    MBScraper().run()
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
