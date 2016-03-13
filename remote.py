from flask import Flask
from flask import render_template
import lirc
app = Flask(__name__)
deviceids = lirc.getids()

@app.route('/')
def index():
    global deviceids
    devices = []
    for dev in deviceids:
        d = {
            'id': dev,
            'name': dev,
        }
        devices.append(d)
        return render_template('index.html', devices=devices)
    

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
