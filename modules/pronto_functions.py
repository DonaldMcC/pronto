# - Coding UTF8 -
#
# - This will contain the code to establish the sequence of actions to send
# - to the cubetto and probably develop the full instruction set and secondly
# - there should be code to send instructions to the cubetto  

import serial
import time

def commandlist(mainblock, functionblock):
    """This combines the mainblock and function block into a single list of commands for
       the cubetto
    >>> commandlist('FLXR','LRF')
    'FLLRFR'
    """

    validcommands = ('F','L','R')  
    functioncommand = 'X'
    finalblock = ''
    warnings = ''

    for char in mainblock:
        if char in validcommands:
            finalblock += char
        elif char == functioncommand:
            finalblock += functionblock
        else:
            warning += 'Invalid character in commands'
        
    return finalblock

def sendcommand(finalblock):
    #TO DO pick-up serial port settings from serial port once working
    ser = serial.Serial(
    port='/dev/ttyUSB1', baudrate=9600)

    ser.isOpen()
    time.Sleep(2)    
    ser.write(finalblock)
    ser.close()

    return
