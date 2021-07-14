from flask import app
import serial, app_logger, json

class SerialPortConnection():
    def __init__(self, params, port_name, baudrate, pause):
        self.params = params
        self.port_name = port_name
        self.baudrate = baudrate
        self.pause = pause
        self.ser = serial.Serial(self.port_name, self.baudrate, timeout=self.pause) 
        self.logger = app_logger.get_logger(__name__) 

    def sendMessage(self, message):
        try:
            self.ser.write(message)
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

    def readMessage(self):
        try:    
            line = self.ser.readline()
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

    def ejection(self):
        try:
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

    def enable_engine(self, url, period):
        try:
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

    def stop(self):
        try:
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

    def software_blocker(self, activity):
        try:
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

    def check_weight(self):
        try:
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

    def get_json(self):
        try:
            a = []
            data = self.ser.readline().decode("utf-8")
            dict_json = json.loads(data)
            return dict_json
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

