from flask import Flask, Response, render_template, url_for, request
from functools import wraps
from datetime import datetime
import time
import os
import netifaces as ni
import csv

app = Flask(__name__)

def check_auth(username, password):
    if username == 'admin' and password == 'admin':
        return True
    return False

def authenticate():
    return Response('Could not verify your username password',401,{'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/time')
@requires_auth
def index():
    action = request.args.get('action', default = 'getCurrentTime')
    date = request.args.get('date', default = '')
    time = request.args.get('time', default = '')

    if action == "getCurrentTime":
        return render_template('index.html')
    elif action == "setCurrentTime":
        dateTime = date + " " + time
        cmdLine = f'timedatectl set-time "{dateTime}"'
        os.system(cmdLine)

        return 'Ok'

@app.route('/time/show')
def time_feed():
    def generate():
        yield datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return Response(generate(), mimetype= 'text')

@app.route('/log')
@requires_auth
def log():
    action = request.args.get('action', default = 'getLog')
    date = request.args.get('date', default = '')
    time = request.args.get('time', default = '')
    activity = request.args.get('activity', default = '')

    def toLogServer(date,time,activity):
        with open('./settings/log.csv', 'a', newline = '') as file:
            writer = csv.writer(file)
            dateTime = date + " " + time
            writer.writerow([dateTime, "server", activity])
            file.close()

    if action == 'getLog':
        with open('settings/log.csv') as file:
            reader = csv.reader(file)
            return render_template('log.html', csv = reader)

    elif action == 'addLog':
        toLogServer(date,time,activity)
        return "Ok"

@app.route('/IPaddress')
@requires_auth
def IPset():
    action = request.args.get('action', default = 'getIP')
    IP = request.args.get('IP', default = '')

    if action == 'getIP':
        ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        return render_template('Ip.html', ip = ip)
    elif action == 'setIP':
        cmd = f'sudo ifconfig eth0 {IP} netmask 255.255.255.0'
        os.system(cmd)
        return "Ok"

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug = True, threaded = True)