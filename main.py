#!/home/max/Загрузки/Python-3.10.2/python
# -*- coding: utf-8 -*-
__version__ = 'v 1.3'
"""
Modbus RTU сканер
MODE 1. Сканирует заданные регистры по одному, выводит строку "None" если регистра не существует
MODE 2. Непрерывное чтение
MODE 3. Циклическая запись и чтение одним запросом
MODE 4. Запись одного регистра
Работает в двух потоках: 
В основном GUI
В дополнительном - сам сканер
"""
# TODO:
#  Добавить запись значений с трансмит окна из БД
import traceback
from time import sleep
import sys

from pymodbus.client.sync import ModbusSerialClient as client_RTU
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSerialPort import QSerialPortInfo

from mainwindow import Ui_MainWindow
import DB_module
import App_modules


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        self.start_mode = None
        self.portList = []
        self.data_array_write = []
        self.number_first_register_write: int = 0
        self.slaves_arr = []
        self.quantity_registers_read: int = 1
        self.number_first_register_read: int = 0
        self.data_for_request = {}

        self.status_work = False
        self.text_window = []
        self.mainthread = MBPool()

        self.hold_check_state: int = 0
        self.input_check_state: int = 0
        self.discrete_check_state: int = 0
        self.coil_check_state: int = 0

        # QtWidgets.QMainWindow.__init__(self, parent)
        # Ui_MainWindow.__init__(self)
        super().__init__()
        # Получаем доступные порты от системы
        ports = QSerialPortInfo().availablePorts()
        for port in ports:
            self.portList.append(port.portName())

        self.setupUi(self)

        self.radio_single_r.toggled.connect(lambda: self.button_state(self.radio_single_r))
        self.radio_cicle_r.toggled.connect(lambda: self.button_state(self.radio_cicle_r))
        self.radio_cicle_rw.toggled.connect(lambda: self.button_state(self.radio_cicle_rw))
        self.radio_single_w.toggled.connect(lambda: self.button_state(self.radio_single_w))
        self.state_button = 0

        self.btn_request.clicked.connect(self.button_request)
        self.btn_stop_req.clicked.connect(lambda: DB_module.change_value_in_db(0))

        self.bRawDataClean.clicked.connect(lambda: self.ptRawData.setPlainText(""))
        self.cbPort.addItems(self.portList)
        self.mainthread.sig_result.connect(self.set_text_window)  # , QtCore.Qt.QueuedConnection
        self.mainthread.sig_while_result.connect(self.set_while_text_window)
        self.mainthread.sig_status_work.connect(self.set_interlock_btn_request)
        # RTU Settings default
        self.current_serial_port: str = "/dev/tnt1"
        self.current_baud_port: int = 9600
        self.current_data_bits: int = 8
        self.current_stop_bits: int = 1
        self.current_parity: str = "None"
        self.current_parity_modify: str = "N"
        self.setting_RTU = {}

    def button_state(self, btn):
        if btn.isChecked():
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

    def button_request(self):
        # Передача выбранных режимов
        self.start_mode = self.state_button
        self.hold_check_state = self.checkBox_hold.checkState()
        self.input_check_state = self.checkBox_inp.checkState()
        self.discrete_check_state = self.checkBox_dis.checkState()
        self.coil_check_state = self.checkBox_coil.checkState()
        # Данные для запроса Modbus
        self.slaves_arr = [self.sbSlaveID.value()]
        self.quantity_registers_read = self.sbCount.value()
        self.number_first_register_read = self.sbAddress.value()
        self.data_array_write = DB_module.get_values_from_db(count=4)
        self.number_first_register_write = 0
        # Ложим в словарь для отправки
        self.data_for_request = {
            # Передача выбранных режимов
            "start_mode": self.start_mode,
            "hold_check_state": self.hold_check_state,
            "input_check_state": self.input_check_state,
            "discrete_check_state": self.discrete_check_state,
            "coil_check_state": self.coil_check_state,
            # Данные для запроса Modbus
            "slaves_arr": self.slaves_arr,
            "quantity_registers_read": self.quantity_registers_read,
            "number_first_register_read": self.number_first_register_read,
            "data_array_write": self.data_array_write,
            "number_first_register_write": self.number_first_register_write,
        }
        # Получаем от GUI текущие настройки RTU
        self.current_serial_port = self.cbPort.currentText()
        self.current_baud_port = int(self.cbBaud.currentText())
        self.current_data_bits = int(self.cbDataBits.currentText())
        self.current_stop_bits = int(self.cbStopBits.currentText())
        self.current_parity = self.cbParity.currentText()
        match self.current_parity:
            case "None":
                self.current_parity_modify = "N"
            case "Even":
                self.current_parity_modify = "E"
            case "Odd":
                self.current_parity_modify = "O"
        self.setting_RTU = {
            "port": '/dev/' + self.current_serial_port,
            "baudrate":  self.current_baud_port,
            "timeout": 0.1,
            "stopbits": self.current_stop_bits,
            "parity": self.current_parity_modify,
        }

        # self.mainthread.__init__(**self.data_for_request)
        self.mainthread.get_setting_from_window = self.setting_RTU  # Отправляем настройки в поток МБ пула
        self.mainthread.data_for_request = self.data_for_request  # Отпраляем данные для запроса
        self.mainthread.start()  # Запускаем МБ пул в другом потоке

    def set_text_window(self, result):
        self.ptRawData.appendPlainText("".join(map(str, result)))  # Получаем данные из потока МБ пула

    def set_while_text_window(self, result):
        self.ptRawData.setPlainText("".join(map(str, result)))  # Получаем данные из потока МБ пула

    def set_interlock_btn_request(self, status_run):
        self.status_work = status_run
        if self.status_work:
            self.btn_request.setEnabled(False)
            self.btn_stop_req.setEnabled(True)
        else:
            self.btn_request.setEnabled(True)
            self.btn_stop_req.setEnabled(False)


class MBPool(QtCore.QThread):
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
    sig_result = QtCore.pyqtSignal(list)
    sig_while_result = QtCore.pyqtSignal(list)
    sig_status_work = QtCore.pyqtSignal(bool)

    # count_obj_of_class = 0  # debug

    def __init__(self):

        # self.count_obj_of_class += 1  # debug
        # print(f"Created obj of MBScraper : {self.count_obj_of_class}")  # debug
        self.data_result = []
        self.traceback_error = None
        self.result = []
        self.result_of_reading = None
        self.slave_id_ = None
        self.error_count = 0
        self.fact_reg = 0
        self.status_work = False
        self.text_window = []
        self.time_diff = 0
        self.stop = DB_module.get_stop_from_db()
        self.method: str = 'rtu'
        # Получаем из другого потока MainWindow
        self.number_first_register_write: int = 0
        self.slaves_arr: list = [1]
        self.quantity_registers_read: int = 1
        self.number_first_register_read: int = 0
        self.data_array_write: list = []

        self.hold_check_state: int = 0
        self.input_check_state: int = 0
        self.discrete_check_state: int = 0
        self.coil_check_state: int = 0
        self.start_mode: int = 0

        super().__init__()

        self.get_setting_from_window = {}
        self.data_for_request = {}
        self.client = None  # client_RTU(Settings_MB.method, **Settings_MB.setting_RTU)

    def __del__(self):
        self.client.close()
        # self.count_obj_of_class -= 1  # debug
        # print(f"Вызван деструктор класса, в памяти осталось объектов: {self.count_obj_of_class}")  # debug

    @App_modules.time_of_function
    def _read_init(self, mode_read_registers):
        self.error_count = 0
        self.data_result = []  # Очищаем список от прошлого вывода
        self.status_work = True

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
                        self.status_work = False
                        return

        self.fact_reg = len(self.data_result) - self.error_count

        App_modules.set_text_to_window(self, mode_read_registers)
        # App_modules.printing_to_console(self, mode_read_registers)

        self.status_work = False

        # self.result = [self.data_result, self.fact_reg, self.traceback_error, self.error_count]

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
                self.status_work = False
                self.sig_status_work.emit(self.status_work)
                break
            self.status_work = True
            # TODO Сделать подсчет количества регистров для записи динамическим
            values = DB_module.get_values_from_db(count=4)
            sleep(0.5)
            data = self.client.readwrite_registers(read_address=self.number_first_register_read,
                                                   read_count=self.quantity_registers_read,
                                                   write_address=self.number_first_register_write,
                                                   write_registers=values,
                                                   unit=self.slaves_arr[0])
            if hasattr(data, "registers"):
                self.text_window = data.registers
                self.sig_while_result.emit(self.text_window)
            else:
                self.traceback_error = traceback.format_exc()
                self.text_window.append(self.traceback_error)
                self.sig_while_result.emit(self.text_window)
            self.text_window = []
            self.sig_status_work.emit(self.status_work)

    def write_regs(self):
        data = self.client.write_registers(self.number_first_register_write,
                                           self.data_array_write, unit=self.slaves_arr[0])
        return str(data)

    def run(self):
        # Селектор режимов
        # Принимем данные из Mainwindow в момент нажатия запроса
        self.client = client_RTU(self.method, **self.get_setting_from_window)
        self.number_first_register_write = self.data_for_request.get("number_first_register_write", 0)
        self.slaves_arr = self.data_for_request.get("slaves_arr", [1])
        self.quantity_registers_read = self.data_for_request.get("quantity_registers_read", 1)
        self.number_first_register_read = self.data_for_request.get("number_first_register_read", 0)
        self.data_array_write = self.data_for_request.get("data_array_write", [])

        self.hold_check_state = self.data_for_request.get("hold_check_state", 0)
        self.input_check_state = self.data_for_request.get("input_check_state", 0)
        self.discrete_check_state = self.data_for_request.get("discrete_check_state", 0)
        self.coil_check_state = self.data_for_request.get("coil_check_state", 0)
        self.start_mode = self.data_for_request.get("start_mode", 0)
        match self.start_mode:
            case 1:  # Сканирует заданные регистры по одному, выводит строку "None" если регистра не существует
                self.status_work = True
                self.sig_status_work.emit(self.status_work)
                if self.hold_check_state != 0:
                    self._read_init(1)
                if self.input_check_state != 0:
                    self._read_init(2)
                if self.discrete_check_state != 0:
                    self._read_init(3)
                if self.coil_check_state != 0:
                    self._read_init(4)
                self.sig_result.emit(self.result)
                self.result = []  # Очищаем текст лист от прошлого запроса
                self.status_work = False
                self.sig_status_work.emit(self.status_work)
            case 2:  # Циклическое чтение
                DB_module.change_value_in_db(1)
                while True:
                    self.status_work = True
                    stop = DB_module.get_stop_from_db()
                    if stop == 0:
                        self.status_work = False
                        self.sig_status_work.emit(self.status_work)
                        break
                    if self.hold_check_state != 0:
                        sleep(0.3)
                        hr = App_modules.read_holding_w(self)
                        self.text_window.append(hr)
                    if self.input_check_state != 0:
                        sleep(0.3)
                        ir = App_modules.read_input_w(self)
                        self.text_window.append(ir)
                    if self.discrete_check_state != 0:
                        sleep(0.3)
                        di = App_modules.read_discrete_inputs_w(self)
                        self.text_window.append(di)
                    if self.coil_check_state != 0:
                        sleep(0.3)
                        cr = App_modules.read_coil_w(self)
                        self.text_window.append(cr)
                    self.sig_while_result.emit(self.text_window)
                    self.text_window = []  # очищаем список от прошлого вывода
                    self.sig_status_work.emit(self.status_work)
            case 3:  # Циклическая запись и чтение одновременно
                DB_module.change_value_in_db(1)
                self.read_write_regs()
            case 4:  # Разовая запись
                self.write_regs()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
