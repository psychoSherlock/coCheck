from flask import Flask, render_template
from app import cowin

kannurID = 297

kannur = cowin(kannurID)
data = kannur.check()

sessionsLen = len(data['sessions'])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', jsonData=data, items=sessionsLen)

if __name__ == '__main__':
    app.debug = True
    app.run()
