from flask import Flask, render_template
from vAPI import cowin
from datetime import date, time
from waitress import serve



kannurID = 297


kannur = cowin(kannurID)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing.html')

@app.route("/district/id=<ID>&date=<date>")
def onDistrict(ID, date):
    district = cowin(date)
    data = district.checkByDis(ID)
    sessionsLen = len(data['sessions']) 

    return render_template('data.html', jsonData=data, items=sessionsLen, time=date)

@app.route("/pincode/pin=<pin>&date=<date>")
def onPin(pin, date):
    district = cowin(date)
    data = district.checkByPin(pin)
    sessionsLen = len(data['centers']) 
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