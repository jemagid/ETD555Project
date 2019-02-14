import application as app
import LabJackPython
import Modbus
import UE9 as ue9
import io
from threading import Thread
global onRamp, constSpeed, downRamp, rotate

def getSignal(up,down,speed,rotation):
    onRamp = up
    constSpeed = speed
    downRamp = down
    rotate = rotation
    sendSignal()

def sendSignal():
    pass
    """
    LJ_ioPUT_DAC_ENABLE  
    LJ_ioGET_DAC_ENABLE 
    LJ_chDAC_BINARY 
    ePut (lngHandle, LJ_ioPUT_DAC, 0, 2.50, 0)
"""

def analogTmp_get():
    pass
"""
    LJ_ioGET_AIN
    LJ_ioPUT_AIN_RANGE    
    LJ_ioGET_AIN_RANGE
"""
def analogCurrent_get():
    pass


def abort():
    pass

def EMERGENCY():
    pass

