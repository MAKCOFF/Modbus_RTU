import traceback


def time_of_function(function):  # Считает время выполнения функции
    def wrapped(*args):
        import time
        start_time = time.perf_counter()
        res = function(*args)
        time_diff = (time.perf_counter() - start_time)
        print("за %.3f sec" % time_diff)
        return res

    return wrapped


def printing_to_console(self, mode_read_registers):
    match mode_read_registers:
        case 1:
            print("Запрошено", len(self.data_result) - 1,
                  "регистров по одному(size 2 BYTE) за каждый запрос \n",
                  "Считано c устройства", self.slave_id_, "HOLDING регистров", self.fact_reg, "\n",
                  self.data_result)
            if self.error_count > 0:
                print("   !pymodbus:\terr_cnt: %s; last tb: %s" % (self.error_count, self.traceback_error))
        case 2:
            print("Запрошено", len(self.data_result) - 1,
                  "регистров по одному(size 2 BYTE) за каждый запрос \n",
                  "Считано c устройства", self.slave_id_, "INPUT регистров", self.fact_reg, "\n", self.data_result)
            if self.error_count > 0:
                print("   !pymodbus:\terr_cnt: %s; last tb: %s" % (self.error_count, self.traceback_error))
        case 3:
            print("Запрошено", len(self.data_result) - 1,
                  "регистров по одному(size 1 BIT) за каждый запрос \n",
                  "Считано c устройства", self.slave_id_, "DISCRETE INPUT регистров", self.fact_reg, "\n",
                  self.data_result)
            if self.error_count > 0:
                print("   !pymodbus:\terrCnt: %s; last tb: %s" % (self.error_count, self.traceback_error))
        case 4:
            print("Запрошено", len(self.data_result) - 1,
                  "регистров по одному(size 1 BIT) за каждый запрос \n",
                  "Считано c устройства", self.slave_id_, "COIL регистров", self.fact_reg, "\n", self.data_result)
            if self.error_count > 0:
                print("   !pymodbus:\terrCnt: %s; last tb: %s" % (self.error_count, self.traceback_error))


def read_holding_w(self, register, quantity_request, slave_id):
    data = self.client.read_holding_registers(register, quantity_request, unit=slave_id)
    assert (not data.isError())
    if hasattr(data, "registers"):
        return "".join(map(str, data.registers))  # Преобразуем из списка в строку
    else:
        self.traceback_error = traceback.format_exc()
        return "None"


def read_input_w(self, register, quantity_request, slave_id):
    data = self.client.read_input_registers(register, quantity_request, unit=slave_id)
    assert (not data.isError())
    if hasattr(data, "registers"):
        return "".join(map(str, data.registers))
    else:
        self.traceback_error = traceback.format_exc()
        return "None"


def read_discrete_inputs_w(self, register, quantity_request, slave_id):
    data = self.client.read_discrete_inputs(register, quantity_request, unit=slave_id)
    assert (not data.isError())
    if hasattr(data, "bits"):
        return "".join(map(str, data.bits))
    else:
        self.traceback_error = traceback.format_exc()
        return "None"


def read_coil_w(self, register, quantity_request, slave_id):
    data = self.client.read_coils(register, quantity_request, unit=slave_id)
    assert (not data.isError())
    if hasattr(data, "bits"):
        return "".join(map(str, data.bits))
    else:
        self.traceback_error = traceback.format_exc()
        return "None"
