#pip install flask pyserial

from flask import Flask, jsonify
import serial
import time

app = Flask(__name__)
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def read_from_arduino():
    data = arduino.readline().decode('utf-8').strip()
    if data:
        temp, humidity = data.split(',')
        return {'temperature': temp, 'humidity': humidity}
    return {'temperature': None, 'humidity': None}

@app.route('/data', methods=['GET'])
def get_data():
    data = read_from_arduino()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
