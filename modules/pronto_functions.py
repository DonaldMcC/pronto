# - Coding UTF8 -
#
# - This will contain the code to establish the sequence of actions to send
# - to the cubetto and probably develop the full instruction set and secondly
# - there should be code to send instructions to the cubetto  


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

    #ser = serial.Serial(port=port, baudrate=baudrate)
    
    #ser.isOpen()
    time.sleep(1)  
    for x in finalblock:
        #ser.write(x)
        time.sleep(0.5)
        
    #ser.close()

    return
