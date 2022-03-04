#!/home/max/Загрузки/Python-3.10.2/python
# -*- coding: utf-8 -*-
__version__ = 'v 1.2'
"""
Modbus RTU сканер
MODE 1. Сканирует заданные регистры по одному, выводит строку "None" если регистра не существует
MODE 2. Непрерывное чтение
MODE 3. Циклическая запись и чтение одним запросом
MODE 4. Одного регистра
"""
import traceback
from time import sleep
import sys

from pymodbus.client.sync import ModbusSerialClient as client_RTU
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread

from mainwindow import Ui_MainWindow
import DB_module
import Settings_MB
import App_modules


class MainWindow(QtWidgets.QMainWindow, client_RTU, Ui_MainWindow):
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

    # number_first_register_write = 0  # default value
    # count_obj_of_class = 0  # debug

    def __init__(self, **kwargs):

        # self.count_obj_of_class += 1  # debug
        # print(f"Created obj of MBScraper : {self.count_obj_of_class}")  # debug

        self.data_result = []
        # self.slaves_arr = kwargs.get('slaves_arr', [17])
        # self.quantity_registers_read = kwargs.get('quantity_registers_read', 10)
        # self.number_first_register_read = kwargs.get('number_first_register_read', 0)
        # self.slaves_arr = [self.sbSlaveID.value()]
        # self.quantity_registers_read = self.sbAddress.value()
        # self.number_first_register_read = self.sbCount.value()
        self.traceback_error = None
        self.result = []
        self.result_of_reading = None
        self.slave_id_ = None
        self.error_count = 0
        self.fact_reg = 0
        self.data_array_write = [50]
        self.number_first_register_write = 0
        self.status_work = False
        self.text_window = []
        self.time_diff = 0

        super().__init__()
        self.setupUi(self)
        # set radiobuttons mode
        # self.radio_single_r.setChecked(True)
        self.radio_single_r.toggled.connect(lambda: self.button_state(self.radio_single_r))
        self.radio_cicle_r.toggled.connect(lambda: self.button_state(self.radio_cicle_r))
        self.radio_cicle_rw.toggled.connect(lambda: self.button_state(self.radio_cicle_rw))
        self.radio_single_w.toggled.connect(lambda: self.button_state(self.radio_single_w))
        self.state_button = 0

        self.btn_request.clicked.connect(lambda: self.run())

        self.slaves_arr = kwargs.get('slaves_arr', [self.sbSlaveID.value()])
        self.quantity_registers_read = kwargs.get('quantity_registers_read', self.sbAddress.value())
        self.number_first_register_read = kwargs.get('number_first_register_read', self.sbCount.value())

        # self.slaves_arr = [self.sbSlaveID.value()]
        # self.quantity_registers_read = self.sbCount.value()
        # self.number_first_register_read = self.sbAddress.value()

        self.bRawDataClean.clicked.connect(lambda: self.ptRawData.setPlainText(""))
        self.btn_stop_req.setEnabled(False)

    def __del__(self):
        self.client.close()
        # self.count_obj_of_class -= 1  # debug
        # print(f"Вызван деструктор класса, в памяти осталось объектов: {self.count_obj_of_class}")  # debug

    @App_modules.time_of_function
    def _read_init(self, mode_read_registers):
        self.error_count = 0
        self.data_result = []
        for slave_id in self.slaves_arr:
            self.slave_id_ = slave_id
            # self.data_result.insert(0, self.slave_id_)  # Вставляем для консоли в начало списка адрес слэйва int
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

        self.fact_reg = len(self.data_result) - self.error_count

        # App_modules.printing_to_console(self, mode_read_registers)
        App_modules.set_text_to_window(self, mode_read_registers)

        self.result = [self.data_result, self.fact_reg, self.traceback_error, self.error_count]
        return self.result

    def read_holding_regs(self, register, slave_id):
        """
        :param register: Текущий регистр для опроса
        :param slave_id: Адрес слэйва
        :return: Возвращает str значение регистра или None при ошибке чтения
        """
        data = self.client.read_holding_registers(register, 1, unit=slave_id)
        # assert (not data.isError())
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
        # assert (not data.isError())
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
        # assert (not data.isError())
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
        # assert (not data.isError())
        if hasattr(data, "bits"):
            data_read.append(data.bits[0])
            return "".join(map(str, data_read))
        else:
            self.traceback_error = traceback.format_exc()
            return "None"

    def read_write_regs(self):
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
                                                   unit=self.slaves_arr[0])
            if hasattr(data, "registers"):
                self.ptRawData.setPlainText(str(data.registers))
            else:
                self.traceback_error = traceback.format_exc()
                self.ptRawData.setPlainText(str(self.traceback_error))

    def write_regs(self):
        data = self.client.write_registers(self.number_first_register_write,
                                           self.data_array_write, unit=self.slaves_arr[0])
        self.ptRawData.setPlainText(str(data))

        #  radiobutton state

    def button_state(self, btn):
        if btn.isChecked():
            # self.btn_request.setEnabled(True)
            match btn.text():
                case "Single read":
                    self.state_button = 1
                case "Cicle read":
                    self.state_button = 2
                case "Cicle read/write":
                    self.state_button = 3
                case "Single write":
                    self.state_button = 4
        self.ptRawData.setPlainText(btn.text())
        # print(self.state_button)

    def button_request_interlock(self):
        pass

    def run(self):
        # Селектор режимов
        self.slaves_arr = [self.sbSlaveID.value()]
        self.quantity_registers_read = self.sbCount.value()
        self.number_first_register_read = self.sbAddress.value()

        match self.state_button:
            case 1:  # Сканирует заданные регистры по одному, выводит строку "None" если регистра не существует
                # self.ptRawData.setPlainText("good 1")
                # print(self.checkBox_hold.checkState())
                if self.checkBox_hold.checkState() != 0:
                    self._read_init(1)
                if self.checkBox_inp.checkState() != 0:
                    self._read_init(2)
                if self.checkBox_dis.checkState() != 0:
                    self._read_init(3)
                if self.checkBox_coil.checkState() != 0:
                    self._read_init(4)
            case 2:  # Непрерывное чтение
                while True:
                    stop = DB_module.get_stop_from_db()
                    if stop == 0:
                        break
                    if self.ui.checkBox_hold.checkState():
                        sleep(0.3)
                        App_modules.read_holding_w(MainWindow)
                    if self.ui.checkBox_inp.checkState():
                        sleep(0.3)
                        App_modules.read_input_w(MainWindow)
                    if self.ui.checkBox_dis.checkState():
                        sleep(0.3)
                        App_modules.read_discrete_inputs_w(MainWindow)
                    if self.ui.checkBox_coil.checkState():
                        sleep(0.3)
                        App_modules.read_coil_w(MainWindow)
            case 3:  # Циклическая запись и чтение одновременно
                self.read_write_regs()
            case 4:  # Разовая запись
                # self.ptRawData.setPlainText("good 4")
                self.write_regs()

    # def request(self):
    #     self.btn_request.clicked.connect(lambda: self.run())

    # def run_app(self):
    #     self.run()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
