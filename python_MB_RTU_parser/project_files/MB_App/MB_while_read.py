import traceback
from time import sleep


def read_holding_w(self, register, quantity_request, slave_id):
    data = self.client.read_holding_registers(register, quantity_request, unit=slave_id)
    assert (not data.isError())  # test that we are not an error
    if hasattr(data, "registers"):
        return "".join(map(str, data.registers))  # Преобразуем из списка в строку
    else:
        self.traceback_error = traceback.format_exc()
        return "None"


def read_input_w(self, register, quantity_request, slave_id):
    data = self.client.read_input_registers(register, quantity_request, unit=slave_id)
    assert (not data.isError())  # test that we are not an error
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


while True:
    sleep(0.5)
