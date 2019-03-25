#Personal Python Files
import excecute as exe
import GUI

global var 
var = bool()

def motorRotation(direction):
    return direction

def start_motor():
    pass

def getCurrent():
    return 0

def getTmp():
    return 0


def getSpeed_onSet(val):  #Get speed from the scale
    GUI.getDown(val)
    
def getUp_onSet(val):    #Get time for upramp scale
    upRampScale.set(val)
    
def getDn_onSet(val):    #Get time for downramp scale
    dnRampScale.set(val)
    
def changeSpeed(opt):    # initializing dutyCycle for slope
    if(opt == -1 ):                         #Calculate downramp speed
        dutyCycle.set(dutyCycle.get() -(speedScale.get()/dnRampScale.get()))
    else:                                   #Calculate upramp speed
       dutyCycle.set(dutyCycle.get() + (speedScale.get()/upRampScale.get()))
    print("Duty Cycle: ", dutyCycle.get(), " %")
    