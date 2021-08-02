from flask import request, json, render_template, redirect, url_for, flash
from app import app
from main import SerialPortConnection
from config import Configuration

import app_logger

config_path = './config.ini'
config = Configuration()
config.load(config_path)
arduino = SerialPortConnection()
logger = app_logger.get_logger(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            if request.form['submit_button'] == 'Загрузить':
                #weight = arduino.check_weight()
                weight = 100
                max_weight = int(config.get('requirements', 'max_weight'))
                if weight > max_weight:
                    arduino.enable_engine()
                else:
                    return render_template('index.html', text='Бутылка отсуствует!')
        return render_template('index.html', text='Положите бутылку в аппарат и нажмите кнопку')
    except Exception as ex:
        logger.error(str(ex))

@app.route("/remoter", methods=['GET', 'POST'])
def remoter():
    try:
        return render_template('remoter.html')
    except Exception as ex:
        logger.error(str(ex))

@app.route("/ejection", methods=['GET', 'POST'])
def ejection():
    try:
        result = arduino.ejection()
        return result
    except Exception as ex:
        logger.error(str(ex))

@app.route("/volume_sensor", methods=['GET', 'POST'])
def volume_sensor():
    try:
        result = arduino.volume_sensor()
        return result
    except Exception as ex:
        logger.error(str(ex))

@app.route("/crusher", methods=['GET', 'POST'])
def crusher():
    try:
        result = arduino.crusher()
        return result
    except Exception as ex:
        logger.error(str(ex))

@app.route("/tensa", methods=['GET', 'POST'])
def tensa():
    try:
        result = arduino.tensa()
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
        if request.method == 'POST':
            return result
        return render_template('json.html', json=result)
    except Exception as ex:
        logger.error(str(ex))

