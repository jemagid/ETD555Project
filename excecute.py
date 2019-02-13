import application as app

global onRamp, constSpeed, downRamp, rotate

def getSignal(up,down,speed,rotation):
    onRamp = up
    constSpeed = speed
    downRamp = down
    rotate = rotation
    sendSignal()

def sendSignal():
    pass

def abort():
    pass

def EMERGENCY():
    pass

