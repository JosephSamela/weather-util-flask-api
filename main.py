import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/<zipcode>')
def zip(zipcode):
    report = os.popen('weather-util ' + zipcode).read()
    report = report.replace('\n','<br>')
    return report

@app.route('/<zipcode>/forcast')
def forcast(zipcode):
    report = os.popen('weather-util -f ' + zipcode).read()
    report = report.replace('\n','<br>').replace(' .','<br>')
    return report

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
