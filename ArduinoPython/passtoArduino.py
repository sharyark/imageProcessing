import serial

arduinoData = serial.Serial('/dev/ttyACM0',9600)

while True:
    cmd = input('enter your comand :')
    cmd += '\r'
    arduinoData.write(cmd.encode())
