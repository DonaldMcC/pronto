# - Coding UTF8 -
#
# - This will contain the code to establish the sequence of actions to send
# - to the cubetto and probably develop the full instruction set and secondly
# - there should be code to send instructions to the cubetto  


import time
import atexit
from Raspi_MotorHAT import Raspi_MotorHAT

mh = Raspi_MotorHAT(addr=0x6f)
lm = mh.getMotor(3)
rm = mh.getMotor(1)


def commandlist(mainblock, functionblock):
    """This combines the mainblock and function block into a single list of commands for
       the cubetto
    >>> commandlist('FLXR','LRF')
    'FLLRFR'
    """

    validcommands = ('F','L','R')  
    functioncommand = 'X'
    finalblock = ''
    warning = ''

    for char in mainblock:
        if char in validcommands:
            finalblock += char
        elif char == functioncommand:
            finalblock += functionblock
        else:
            warning += 'Invalid character in commands'
        
    return finalblock


def sendcommand(finalblock, port, baudrate):
    # This sends the command to the cubetto   
    # TODO put some try catch and error reporting around this

    # ser = serial.Serial(port=port, baudrate=baudrate)
    
    #ser.isOpen()
    time.sleep(1)  
    for x in finalblock:
        #ser.write(x)
        time.sleep(0.5)
        
    #ser.close()
    return


def sendpicommand(finalblock):
    # This sends the command to pi which has motors attached
    time.sleep(1)
    for x in finalblock:
        if x == 'F':
            go_forward()
        elif x == 'B':
            go_backward()
        elif x == 'R':
            go_right()
        elif x == 'L':
            go_left()
        else:
            print('An unknown command was attempted')
        time.sleep(2)
    return


def turn_off_motors():
    lm.run(Raspi_MotorHAT.RELEASE)
    rm.run(Raspi_MotorHAT.RELEASE)

atexit.register(turn_off_motors)

def go_forward(speed=150, secs=1):
    lm.setSpeed(speed)
    rm.setSpeed(speed)
    lm.run(Raspi_MotorHAT.FORWARD)
    rm.run(Raspi_MotorHAT.FORWARD)
    time.sleep(secs)
    turn_off_motors()

def go_backward(speed=150, secs=1):
    lm.setSpeed(speed)
    rm.setSpeed(speed)
    lm.run(Raspi_MotorHAT.BACKWARD)
    rm.run(Raspi_MotorHAT.BACKWARD)
    time.sleep(secs)
    turn_off_motors()

def go_left(speed=150, secs=1):
    lm.setSpeed(speed)
    rm.setSpeed(speed)
    lm.run(Raspi_MotorHAT.BACKWARD)
    rm.run(Raspi_MotorHAT.FORWARD)
    time.sleep(secs)
    turn_off_motors()

def go_right(speed=150, secs=1):
    lm.setSpeed(speed)
    rm.setSpeed(speed)
    lm.run(Raspi_MotorHAT.FORWARD)
    rm.run(Raspi_MotorHAT.BACKWARD)
    time.sleep(secs)
    turn_off_motors()
\\\\\\\\\\\\\\\\\\\\\\\\\