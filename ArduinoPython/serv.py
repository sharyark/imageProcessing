from cmath import pi
from pyfirmata import Arduino , SERVO,util
from time import sleep

port = '/dev/ttyACM1'
pin = 10
board = Arduino(port)
board.digital[pin].mode = SERVO

def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)
    
rotateservo(pin,50)
while True:
    x = input('input : ')
    if x=='1':
        for i in range(50,160):
            rotateservo(pin,i)
    elif x=='2':
        for i in reversed(range(50,160)):
            rotateservo(pin,i)
    elif x=='3':
        for i in range(0,270):
            rotateservo(pin,i)
        
