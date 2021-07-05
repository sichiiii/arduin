from flask import app
import serial, app_logger

class SerialPortConnection():
    def __init__(self, params, port_name, baudrate, pause):
        self.params = params
        self.port_name = port_name
        self.baudrate = baudrate
        self.pause = pause
        #self.ser = serial.Serial(self.port_name, self.baudrate, timeout=self.pause) 
        self.logger = app_logger.get_logger(__name__) 

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

    def ejection(self):
        try:
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))

    def enable_engine(self, url, period):
        try:
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))

    def stop(self):
        try:
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))

    def software_blocker(self, activity):
        try:
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))

    def check_weight(self):
        try:
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))