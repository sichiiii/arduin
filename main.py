from flask import app
import serial, app_logger, json
from config import Configuration

config_path = './config.ini'

class SerialPortConnection():
    def __init__(self):
        self.config = Configuration()
        self.config.load(config_path)
        self.params = self.config.get('arduino', 'params')
        self.port_name = self.config.get('arduino', 'port')
        self.baudrate = self.config.get('arduino', 'baudrate')
        self.pause = self.config.get('arduino', 'pause')
        self.ser = serial.Serial(self.port_name, self.baudrate, timeout=int(self.pause)) 
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
            data = {"command":'ejection', "value":"1"}
            data=json.dumps(data)
            self.ser.write(data.encode('ascii'))
            incoming = self.ser.readline().decode("utf-8")
            print (incoming)
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

    def enable_engine(self, url, period):
        try:
            data = {"command":'enable_engine', "value":"1"}
            data=json.dumps(data)
            self.ser.write(data.encode('ascii'))
            incoming = self.ser.readline().decode("utf-8")
            print (incoming)
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

    def stop(self):
        try:
            data = {"command":'stop', "value":"1"}
            data=json.dumps(data)
            print(data)
            self.ser.write(data.encode('ascii'))
            incoming = self.ser.readline().decode("utf-8")
            print (incoming)
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

    def software_blocker(self, activity):
        try:
            data = {"command":'software_blocker', "value":"1"}
            data=json.dumps(data)
            self.ser.write(data.encode('ascii'))
            incoming = self.ser.readline().decode("utf-8")
            print (incoming)
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

    def check_weight(self):
        try:
            data = {"command":'check_weight', "value":"1"}
            data=json.dumps(data)
            self.ser.write(data.encode('ascii'))
            incoming = self.ser.readline().decode("utf-8")
            print (incoming)
            return {'status':'ok'}
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

    def get_json(self):
        try:
            data = self.ser.readline().decode("utf-8")
            dict_json = json.loads(data)
            return dict_json
        except Exception as ex:
            self.logger.error(str(ex))
            return {'status':'error'}

