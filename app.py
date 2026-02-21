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
    try:
        arduino = serial.Serial('COM3', 9600, timeout=1)
        time.sleep(2)
        print("Arduino connected")
    except serial.SerialException as e:
        print("Arduino connection failed:", e)
        arduino = None

def read_arduino():
    global latest_data, arduino

    while True:
        try:
            if not arduino:
                time.sleep(1)
                continue

            line = arduino.readline().decode(errors="ignore").strip()
            if not line:
                continue

            print("RAW:", line)

            for part in line.split("|"):
                part = part.strip()

                if part.startswith("TemperatureC"):
                    latest_data["temperature"] = part.split(":")[1].strip()

                elif part.startswith("Humidity"):
                    latest_data["humidity"] = part.split(":")[1].replace("%", "").strip()

        except serial.SerialException as e:
            print("Serial error:", e)
            arduino = None

        except Exception as e:
            print("Parse error:", e)




@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def data():
    return jsonify(latest_data)
@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store"
    return response



if __name__ == "__main__":
    connect_arduino()
    threading.Thread(target=read_arduino, daemon=True).start()

    # 🔴 VERY IMPORTANT LINE
    app.run(debug=True, use_reloader=False)
