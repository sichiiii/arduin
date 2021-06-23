from flask import request, json, render_template
from app import app
from main import SerialPortConnection

arduino = SerialPortConnection(5, '5', 5, 5)  #params, port, baudrate, pause 

@app.route("/home", methods=['POST'])
def create_report():
    try:
        json_data = arduino.readMessage()
        return json_data
    except Exception as ex:
        return {'status': 'error', 'message': str(ex)}