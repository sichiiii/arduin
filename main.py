from flask import app
import serial, app_logger

class SerialPortConnection():
    def __init__(self, params, port_name, baudrate, pause):
        self.params = params
        self.port_name = port_name
        self.baudrate = baudrate
        self.pause = pause
        self.ser = serial.Serial(self.port_name, self.baudrate, timeout=self.pause) 
        self.logger = app_logger.logger(__name__) 

    def sendMessage(self, message):
        try:
            self.ser.write(message)
        except Exception as ex:
            self.logger.error(str(ex))

    def readMessage(self):
        try:    
            line = self.ser.readline()
        except Exception as ex:
            self.logger.error(str(ex))