from flask import request, json, render_template
from app import app
from main import SerialPortConnection
import app_logger

arduino = SerialPortConnection(5, '5', 5, 5)  #params, port, baudrate, pause 
logger = app_logger.logger(__name__)

@app.route("/home", methods=['POST'])
def create_report():
    try:
        json_data = arduino.readMessage()
        return json_data
    except Exception as ex:
        logger.error(str(ex))