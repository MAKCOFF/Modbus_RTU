import traceback


def time_of_function(function):  # Считает время выполнения функции
    def wrapped(self, *args):
        import time
        start_time = time.perf_counter()
        res = function(self, *args)
        self.time_diff = (time.perf_counter() - start_time)
        self.ptRawData.appendPlainText("Время работы %.3f sec" % self.time_diff)
        # print("за %.3f sec" % time_diff)
        return res

    return wrapped


def set_text_to_window(self, mode_read_registers):
    match mode_read_registers:
        case 1:
            self.ptRawData.appendPlainText(
                f"Запрошено {self.quantity_registers_read} регистров по одному(size 2 BYTE) за каждый запрос \n Считано c устройства {self.slave_id_}  HOLDING регистров {self.fact_reg}  \n {self.data_result}")
            if self.error_count > 0:
                self.ptRawData.appendPlainText(
                    f"\n !pymodbus:\n err_cnt: {self.error_count} \n tb: {self.traceback_error}")
        case 2:
            self.ptRawData.appendPlainText(
                f"Запрошено {self.quantity_registers_read} регистров по одному(size 2 BYTE) за каждый запрос \n Считано c устройства {self.slave_id_}  INPUT регистров {self.fact_reg}  \n {self.data_result}")
            if self.error_count > 0:
                self.ptRawData.appendPlainText(
                    f"\n !pymodbus:\n err_cnt: {self.error_count} \n tb: {self.traceback_error}")
        case 3:
            self.ptRawData.appendPlainText(
                f"Запрошено {self.quantity_registers_read} регистров по одному(size 1 BIT) за каждый запрос \n Считано c устройства {self.slave_id_}  DISCRETE INPUTS {self.fact_reg}  \n {self.data_result}")
            if self.error_count > 0:
                self.ptRawData.appendPlainText(
                    f"\n !pymodbus:\n err_cnt: {self.error_count} \n tb: {self.traceback_error}")
        case 4:
            self.ptRawData.appendPlainText(
                f"Запрошено {self.quantity_registers_read} регистров по одному(size 1 BIT) за каждый запрос \n Считано c устройства {self.slave_id_}  COIL регистров {self.fact_reg}  \n {self.data_result}")
            if self.error_count > 0:
                self.ptRawData.appendPlainText(
                    f"\n !pymodbus:\n err_cnt: {self.error_count} \n tb: {self.traceback_error}")


def printing_to_console(self, mode_read_registers):  # Для консоли. сейчас НЕ используется!!!
    match mode_read_registers:
        case 1:
            print(
                "Запрошено", self.quantity_registers_read,
                "регистров по одному(size 2 BYTE) за каждый запрос \n",
                "Считано c устройства", self.slave_id_, "HOLDING регистров", self.fact_reg, "\n",
                self.data_result)
            if self.error_count > 0:
                print("   !pymodbus:\terr_cnt: %s; last tb: %s" % (self.error_count, self.traceback_error))
        case 2:
            print(
                "Запрошено", self.quantity_registers_read,
                "регистров по одному(size 2 BYTE) за каждый запрос \n",
                "Считано c устройства", self.slave_id_, "INPUT регистров", self.fact_reg, "\n", self.data_result)
            if self.error_count > 0:
                print("   !pymodbus:\terr_cnt: %s; last tb: %s" % (self.error_count, self.traceback_error))
        case 3:
            print(
                "Запрошено", self.quantity_registers_read,
                "регистров по одному(size 1 BIT) за каждый запрос \n",
                "Считано c устройства", self.slave_id_, "DISCRETE INPUT регистров", self.fact_reg, "\n",
                self.data_result)
            if self.error_count > 0:
                print("   !pymodbus:\terrCnt: %s; last tb: %s" % (self.error_count, self.traceback_error))
        case 4:
            print(
                "Запрошено", self.quantity_registers_read,
                "регистров по одному(size 1 BIT) за каждый запрос \n",
                "Считано c устройства", self.slave_id_, "COIL регистров", self.fact_reg, "\n", self.data_result)
            if self.error_count > 0:
                print("   !pymodbus:\terrCnt: %s; last tb: %s" % (self.error_count, self.traceback_error))


def read_holding_w(self):
    data = self.client.read_holding_registers(self.number_first_register_read,
                                              self.quantity_registers_read,
                                              unit=self.slave_id_)
    assert (not data.isError())
    if hasattr(data, "registers"):
        return data.registers
    else:
        self.traceback_error = traceback.format_exc()
        return "None"


def read_input_w(self):
    data = self.client.read_input_registers(self.number_first_register_read,
                                            self.quantity_registers_read,
                                            unit=self.slave_id_)
    assert (not data.isError())
    if hasattr(data, "registers"):
        return data.registers
    else:
        self.traceback_error = traceback.format_exc()
        return "None"


def read_discrete_inputs_w(self):
    data = self.client.read_discrete_inputs(self.number_first_register_read,
                                            self.quantity_registers_read,
                                            unit=self.slave_id_)
    assert (not data.isError())
    if hasattr(data, "bits"):
        return data.bits
    else:
        self.traceback_error = traceback.format_exc()
        return "None"


def read_coil_w(self):
    data = self.client.read_coils(self.number_first_register_read,
                                  self.quantity_registers_read,
                                  unit=self.slave_id_)
    assert (not data.isError())
    if hasattr(data, "bits"):
        return data.bits
    else:
        self.traceback_error = traceback.format_exc()
        return "None"
