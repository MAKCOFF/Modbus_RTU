def time_of_function(function):  # Считает время выполнения функции
    def wrapped(*args):
        import time
        start_time = time.perf_counter()
        res = function(*args)
        time_diff = (time.perf_counter() - start_time)
        print("за %.3f sec" % time_diff)
        return res
    return wrapped


def printing_to_cons(function):  # NOT Used !!!
    def wrapped(self, *args):
        # res = []
        res = function(*args)
        print("Запрошено", len(self.data_result) - 1,
              "регистров по одному(size 2 BYTE) за каждый запрос \n",
              "Считано c устройства", self.slave_id_, "HOLDING регистров", self.fact_reg, "\n",
              self.data_result)
        if self.error_count > 0:
            print("   !pymodbus:\terr_cnt: %s; last tb: %s" % (self.error_count, self.traceback_error))
        return res

    return wrapped
    # self.result = [self.data_result, fact_reg, self.traceback_error, error_count]


def printing_to_console(self):
    match self.mode_read_registers:
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
