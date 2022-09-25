import time
import serial
from vpython import *
import numpy as np
arduinoData = serial.Serial('/dev/ttyACM0',9600)
time.sleep(1)
data = []
arLen = 2
arWid = .1
Arrow = arrow(length=arLen,shaftwidth=arWid,color=color.red,axis=vector(-1,0,0))
# tube = cylinder(color=color.green,radius=1,length=5,axis=vector(0,1,0))
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
    print(voltageAnalogue)
    theta = -2*np.pi/3069*voltageAnalogue+5*np.pi/6
    Arrow.axis = vector(arLen*np.cos(theta),arLen*np.sin(theta),0)

    # for theta in np.linspace(5*np.pi/6,np.pi/6,100):
    #     rate(20)
    #     Arrow.axis = vector(arLen*np.cos(theta),arLen*np.sin(theta),0)
    # for theta in reversed(np.linspace(5*np.pi/6,np.pi/6,100)):
    #     rate(20)
    #     Arrow.axis = vector(arLen*np.cos(theta),arLen*np.sin(theta),0)