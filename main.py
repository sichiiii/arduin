import serial

class SerialPortConnection():
    def __init__(self, params, port_name, baudrate, pause):
        self.params = params
        self.port_name = port_name
        self.baudrate = baudrate
        self.pause = pause
        self.ser = serial.Serial(self.port_name, self.baudrate, timeout=self.pause)  

    def sendMessage(self, message):
        self.ser.write(message)

    def readMessage(self):
        line = self.ser.readline()