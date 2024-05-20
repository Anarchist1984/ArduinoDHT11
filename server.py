@app.route('/data')
def get_data():
    try:
        # Read data from the micro:bit
        data = ser.readline().decode('utf-8').strip()
        print('Received data:', data)  # Debugging output
        parts = data.split(',')
        if len(parts) == 2:
            temperature, humidity = parts
            print({'temperature': temperature, 'humidity': humidity})  # Debugging output
            return jsonify({'temperature': temperature, 'humidity': humidity})
        else:
            raise ValueError('Expected 2 parts, got {}'.format(len(parts)))
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': str(e)})
