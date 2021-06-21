# Author Athul Prakash NJ

from flask import Flask, render_template
from vapi import api
from vapi import getDistricts
from datetime import date, time
from waitress import serve

kannurID = 297

mappings = getDistricts()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing.html', maps=mappings)

@app.route("/district/id=<ID>&date=<date>")
def onDistrictId(ID, date):
    district = api(date)
    data = district.checkByDistrictId(ID)
    sessionsLen = len(data['sessions']) 

    return render_template('data.html', jsonData=data, items=sessionsLen, time=date)

@app.route("/pincode/pin=<pin>&date=<date>")
def onPincode(pin, date):
    district = api(date)
    data = district.checkByPincode(pin)
    sessionsLen = len(data['sessions']) 
    return render_template('data.html', jsonData=data, items=sessionsLen, time=date)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

port = '8080'
hostIp = '0.0.0.0'

if __name__ == '__main__':
    print(f"Serving app... on http://{hostIp}:{port}")
    with open('debug/start.log', 'a') as startLog:
        startLog.write(f"\nStarted on {date.today().strftime('%d-%m-%y')}")
        startLog.close()
    serve(app, host=hostIp, port=port)
    # FOr debug:><
    # app.run(host=hostIp, port=port, debug=True)