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
            url = request.form['url']
            period = request.form['period']
            if not url:
                json_data = request.get_json()
                url = json_data['url']
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
            activity = request.form.getlist('checkbox')
            if not activity:
                json_data = request.get_json()
                activity = json_data['activity']
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

@app.route("/json", methods=['GET', 'POST'])
def json():
    try:
        result = arduino.get_json()
        #result = {"word1":"hello", "word2":"bro", "word3":"hello", "word4":"bro", "word5":"hello", "word6":"bro", "word7":"hello", "word8":"bro"}
        if request.method == 'POST':
            return result
        return render_template('json.html', json=result)
    except Exception as ex:
        logger.error(str(ex))

@app.route("/remoter", methods=['GET', 'POST'])
def remoter():
    try:
        if request.method == 'POST':
            print('yes')
        return render_template('remoter.html')
    except Exception as ex:
        logger.error(str(ex))


@app.route("/asd", methods=['GET', 'POST'])
def asd():
    try:
        arduino.asd()
        return 'hi'
    except Exception as ex:
        logger.error(str(ex))