#pip install flask pyserial

from flask import Flask, jsonify
import serial

app = Flask(__name__)
ser = serial.Serial('/dev/ttyACM0', 115200)  # Adjust port as needed

@app.route('/data')
def get_data():
    try:
        # Read data from the micro:bit
        data = ser.readline().decode('utf-8').strip()
        temperature, humidity = data.split(',')
        return jsonify({'temperature': temperature, 'humidity': humidity})
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
