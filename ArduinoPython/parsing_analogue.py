from cProfile import label
import time
from turtle import color
import serial
from vpython import *

arduinoData = serial.Serial('/dev/ttyACM0',9600)
time.sleep(1)
data = []
tube = cylinder(color=color.green,radius=1,length=5,axis=vector(0,1,0))
lab = label(text='5-VOLTs')
lab.color = color.red
while True:
    while (arduinoData.inWaiting()==0):
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket,'utf-8')
    dataPacket = dataPacket.strip('\r\n')
    if dataPacket == '':
        dataPacket = '.2'
    voltageAnalogue = int(float(dataPacket))
    voltageDigital = (5./1023.)*voltageAnalogue
    print('volagte is :',voltageDigital)
    # print(dataPacket)
    if voltageDigital == 0:
        voltageDigital = .32
    voltageDigital = round(voltageDigital,1)
    tube.length=voltageDigital
    lab.text = str(voltageDigital)+'-VOLTs'
    