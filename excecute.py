#STD Python Librayies
from threading import Thread

# Personal Python Files
import application as app

#Downloaded libraryies
import LabJackPython
import Modbus
import UE9 as ue9


global onRamp, constSpeed, downRamp, rotate

#Get all CONVERTED Singals for the Labjack unit to use
def getSignal(up,down,speed,rotation):
    onRamp = up
    constSpeed = speed
    downRamp = down
    rotate = rotation
    sendSignal()

#Send all signals to the Labjack unit
def sendSignal():
    pass
    """
    LJ_ioPUT_DAC_ENABLE  
    LJ_ioGET_DAC_ENABLE 
    LJ_chDAC_BINARY 
    ePut (lngHandle, LJ_ioPUT_DAC, 0, 2.50, 0)
"""
# Get the Temperature on all the MOSFETS and displaces it on the Python GUI
def analogTmp_get():
    pass
"""
    LJ_ioGET_AIN
    LJ_ioPUT_AIN_RANGE    
    LJ_ioGET_AIN_RANGE
"""
# Get the current draw before the motor and displaces it on the Python GUI
def analogCurrent_get():
    pass

# Hults all functionallity till the user resets the phicals switch on the breadboard
def abort():
    pass

#Incase of any emergancy this function is used to stop all functionality of the motor, breadboard and ciruit, by cutting of any and all power.
#To reinstate the motor for regular use the user must reset the breadboard and confirt the change on the python GUI 
def EMERGENCY():
    pass

