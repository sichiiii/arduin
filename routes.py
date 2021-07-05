from flask import request, json, render_template
from app import app
from main import SerialPortConnection
import app_logger

arduino = SerialPortConnection(5, '5', 5, 5)  #params, port, baudrate, pause 
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
            try:
                url = request.form['url']
                period = request.form['period']
                if not url:
                    json_data = request.get_json()
                    url = json_data['url']
            except:
                print('...')
            result = arduino.enable_engine(url, period)
            return {'status':'ok'}
        return render_template('enable_engine.html')
    except Exception as ex:
        logger.error(str(ex))

@app.route("/stop", methods=['GET', 'POST'])
def stop():
    try:
        result = arduino.stop()
        return result
    except Exception as ex:
        logger.error(str(ex))

@app.route("/software_blocker", methods=['GET', 'POST'])
def software_blocker():
    try:
        if request.method == 'POST':
            try:
                activity = request.form.getlist('checkbox')
                if not activity:
                    json_data = request.get_json()
                    activity = json_data['activity']
            except Exception as ex:
                print(str(ex))
            print(activity)
            result = arduino.software_blocker(activity)
            return {'status':'ok'}
        return render_template('software_blocker.html')
    except Exception as ex:
        logger.error(str(ex))

@app.route("/check_weight", methods=['GET', 'POST'])
def check_weight():
    try:
        result = arduino.check_weight()
        return result
    except Exception as ex:
        logger.error(str(ex))