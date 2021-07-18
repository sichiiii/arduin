import time
import json
import serial
from pprint import pprint
import random

if __name__ == "__main__":
    print ("Ready...")
    ser  = serial.Serial("/dev/ttyUSB0", baudrate= 9600, 
           timeout=2.5, 
           parity=serial.PARITY_NONE, 
           bytesize=serial.EIGHTBITS, 
           stopbits=serial.STOPBITS_ONE
        )
    data = {}
    data["operation"] = "sequence"
    data=json.dumps(data)
    print (data)
    ser.write(data.encode('ascii'))
    ser.flush()
    try:
        incoming = ser.readline().decode("utf-8")
        print (json.dumps(incoming))
        print('hiP')
    except Exception as e:
        print ('hi')
        pass
