from flask import request, json, render_template
from app import app
from main import SerialPortConnection
import app_logger

arduino = SerialPortConnection(5, '/dev/ttyUSB0', 9600, 1)  #params, port, baudrate, pause 
logger = app_logger.get_logger(__name__)

@app.route("/ejection", methods=['GET', 'POST'])
def ejection():
    try:
        result = arduino.ejection()
        return result
    except Exception as ex:
        logger.error(str(ex))

@app.route("/enable_engine", methods=['GET', 'POST'])
def enable_engine():
    try:
        if request.method == 'POST':
            message = {"command": 'enable_engine', "value":1}
            url = request.form['url']
            period = request.form['period']
            if not url:
                json_data = request.get_json()
                url = json_data['url']
            result = arduino.enable_engine(url, period, message)
            return {'status':'ok'}
        return render_template('enable_engine.html')
    except Exception as ex:
        logger.error(str(ex))

@app.route("/stop", methods=['GET', 'POST'])
def stop():
    try:
        message = {"command": 'stop', "value":1}
        result = arduino.stop(message)
        return result
    except Exception as ex:
        logger.error(str(ex))

@app.route("/software_blocker", methods=['GET', 'POST'])
def software_blocker():
    try:
        if request.method == 'POST':
            message = {"command": 'software_blbocker', "value":1}
            activity = request.form.getlist('checkbox')
            if not activity:
                json_data = request.get_json()
                activity = json_data['activity']
            result = arduino.software_blocker(activity, message)
            return {'status':'ok'}
        return render_template('software_blocker.html')
    except Exception as ex:
        logger.error(str(ex))

@app.route("/check_weight", methods=['GET', 'POST'])
def check_weight():
    try:
        message = {"command": 'check_weight', "value":1}
        result = arduino.check_weight(message)
        return result
    except Exception as ex:
        logger.error(str(ex))

@app.route("/json", methods=['GET', 'POST'])
def json():
    try:
        result = arduino.get_json()
        if request.method == 'POST':
            return result
        return render_template('json.html', json=result)
    except Exception as ex:
        logger.error(str(ex))