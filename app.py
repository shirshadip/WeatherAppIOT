from flask import Flask, render_template, jsonify
import serial
import time
import threading

app = Flask(__name__)

arduino = None
latest_data = {
    "temperature": "--",
    "humidity": "--"
}

def connect_arduino():
    global arduino
    arduino = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)

def read_arduino():
    global latest_data
    while True:
        try:
            if arduino and arduino.in_waiting:
                line = arduino.readline().decode().strip()

                if "Temperature" in line:
                    parts = line.split("|")
                    temp = parts[0].split(":")[1].replace("°C", "").strip()
                    hum = parts[1].split(":")[1].replace("%", "").strip()

                    latest_data["temperature"] = temp
                    latest_data["humidity"] = hum
        except:
            pass


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def data():
    return jsonify(latest_data)


if __name__ == "__main__":
    connect_arduino()
    threading.Thread(target=read_arduino, daemon=True).start()

    # 🔴 VERY IMPORTANT LINE
    app.run(debug=True, use_reloader=False)
