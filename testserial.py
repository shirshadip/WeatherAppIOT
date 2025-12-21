import serial

s = serial.Serial('COM3', 9600)
print("Connected!")
s.close()
