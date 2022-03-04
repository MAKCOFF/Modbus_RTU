from PyQt5.QtSerialPort import QSerialPortInfo

method: str = 'rtu'


class SettingsRTU(QSerialPortInfo):

    def __init__(self):
        self.portList = []

        super().__init__()
        ports = QSerialPortInfo().availablePorts()
        for port in ports:
            self.portList.append(port.portName())
        # print(self.portList)


setting_RTU = {
    "port": '/dev/tnt1',  # for Linux /dev/ttyS1
    "baudrate": 9600,
    "timeout": 0.1,
    "stopbits": 1,
    "parity": 'N',
}
