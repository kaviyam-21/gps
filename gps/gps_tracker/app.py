from flask import Flask, render_template, jsonify
import serial

app = Flask(__name__)

# Initialize serial port for GPS device
serial_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gps-data')
def gps_data():
    # Read data from GPS device
    gps_data = serial_port.readline().decode('utf-8').strip()
    
    # Parse the GPS data if available
    if gps_data:
        latitude, longitude = parse_gps_data(gps_data)
        return jsonify({'latitude': latitude, 'longitude': longitude})
    
    return jsonify({'latitude': None, 'longitude': None})

def parse_gps_data(data):
    # Implement parsing logic based on your GPS device's output
    return data.split(',')

if __name__ == '__main__':
    app.run(debug=True)
