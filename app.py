# Author Athul Prakash NJ

from flask import Flask, render_template
#from waitress import serve


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing.html')

@app.route("/district/id=<ID>&date=<date>")
def onDistrictId(ID, date):
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={ID}&date={date}"
    return render_template('data.html',time=date, url=url)

@app.route("/pincode/pin=<pin>&date=<date>")
def onPincode(pin, date):
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin}&date={date}"
    return render_template('data.html',time=date, url=url)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

#port = '8080'
#hostIp = '0.0.0.0'

#if __name__ == '__main__':
#    print(f"Serving app... on http://{hostIp}:{port}")
#    with open('debug/start.log', 'a') as startLog:
#        startLog.write(f"\nStarted on {date.today().strftime('%d-%m-%y')}")
#        startLog.close()
#    serve(app, host=hostIp, port=port)
    # FOr debug:><
    #app.run(host=hostIp, port=port, debug=True)
