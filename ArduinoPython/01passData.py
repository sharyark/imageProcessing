import time
import serial

arduinoData = serial.Serial('/dev/ttyACM0',9600)
time.sleep(1)
data = []
while True:
    while (arduinoData.inWaiting()==0):
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket,'utf-8')
    print(dataPacket.strip('\r\n'))

    for i in dataPacket.strip('\r\n'):
        data.append(int(i))
    
    print(data)