from flask import Flask, render_template
from vAPI import cowin
from datetime import date
from waitress import serve



kannurID = 297


kannur = cowin(kannurID)
app = Flask(__name__)

@app.route('/')
def index():
    today = date.today().strftime('%d-%m-%y')
    kannur.time = today # For date time format    
    data = kannur.check()
    sessionsLen = len(data['sessions']) 
    return render_template('index.html', jsonData=data, items=sessionsLen, time=today)

@app.route("/date/<on>")
def onDate(on):
    kannur.time = on
    data = kannur.check()
    sessionsLen = len(data['sessions']) 
    return render_template('index.html', jsonData=data, items=sessionsLen, time=on)

port = '8080'

if __name__ == '__main__':
    print("Serving app...")
    with open('debug/start.log', 'a') as startLog:
        startLog.write(f"\nStarted on {date.today().strftime('%d-%m-%y')}")
        startLog.close()
    serve(app, host='0.0.0.0', port=port)