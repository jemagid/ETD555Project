import excecute as exe
import GUI

global var 
var = bool()

def clockwise_Rotation():
    var = True

def counter_clockwise_Rotation():
    var = False

def start_motor():
    up = GUI.getUp()
    down = GUI.getDown()
    speed = GUI.getSpeed()
    if var == True:
        exe.getSignal(up,down,speed,var)
    else:
        speed *= -1
        exe.getSignal(up,down,speed,var)


def getCurrent():
    return 0

def getTmp():
    return 0
    
