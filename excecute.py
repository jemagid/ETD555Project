#STD Python Librayies
from threading import Thread
from tkinter import messagebox as mb

#Personal Python Files
import GUI as window

#Downloaded libraryies
import LabJackPython
import ue9

global onRamp, constSpeed, downRamp, rotate

#Get all CONVERTED Singals for the Labjack unit to use
def getSignal(up,down,speed,rotation,direction):
    onRamp = up
    constSpeed = speed
    downRamp = down
    rotate = rotation
    sendSignal(direction)

#Send all signals to the Labjack unit
def sendSignal(voltage):
    if voltage is not 0:
        window.start("stop","disabled")
    """
    ue9.ue9().singleIO(5,0,DAC=voltage)
    """

# Get the current draw before the motor and displaces it on the Python GUI
def getCur():
    pass

def motorDirection(direction):
    if direction == 1:
        window.clockwise("disabled")
        window.counterClockwise("active")
    if direction == -1:
        window.clockwise("active")
        window.counterClockwise("disabled")

def reset(voltage):
        pass
        """
    if  ue9.ue9().singleIO(2,1) != 0:
        ue9.ue9().singleIO(4,0,DAC=voltage)
        window.counterClockwise("enabled")
        window.clockwise("enabled")
        window.start("start","enabled")
    else:
        mb._show(message="RESET BUTTON NOT PRESSED!")
    """
    

#Incase of any emergancy this function is used to stop all functionality of the motor, breadboard and ciruit, by cutting of any and all power.
#To reinstate the motor for regular use the user must reset the breadboard and confirt the change on the python GUI 
def EMERGENCY(stop):
    if stop == 0:
        window.counterClockwise("disabled")
        window.clockwise("disabled")
        window.start("STOP","disabled")
    """
    if LabJackPython.UE9().singleIO(2,0) != 0:
        ue9.ue9().singleIO(4,0,DAC=0)
        """


