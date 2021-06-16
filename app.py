from flask import Flask, render_template
from vAPI import cowin
from datetime import date


kannurID = 297


kannur = cowin(kannurID)
app = Flask(__name__)

@app.route('/')
def index():
    today = date.today().strftime('%d-%m-%y') # For date time format    
    data = kannur.check(today)
    sessionsLen = len(data['sessions']) 
    return render_template('index.html', jsonData=data, items=sessionsLen, time=today)

@app.route("/date/<on>")
def onDate(on):
    data = kannur.check(on)
    sessionsLen = len(data['sessions']) 
    return render_template('index.html', jsonData=data, items=sessionsLen, time=on)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
