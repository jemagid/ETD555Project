"""
FIO0 - Start - Pin 6
FIO2 - Direction - Pin 5
FIO4 Emergency Stop - Pin 4
FIO6 - Power - Pin 3
AIN - Current - Pin 12
"""
import ue9
import LabJackPython as lj
device = ue9.ue9()

def deviceStartConifg():
    resetLabjackConfig()
    deviceEnable(True)
    deviceDirection(True)

def resetLabjackConfig(): lj.ePut(device.lngHandle, lj.LJ_ioPIN_CONFIGURATION_RESET, 0, 0, 0)

def deviceDirection(Direction):
    lj.ePut (device.lngHandle, lj.LJ_ioPUT_ANALOG_ENABLE_BIT, 5, 0, 0)
    if Direction is 1:
        lj.AddRequest(device.lngHandle, lj.LJ_ioPUT_DIGITAL_BIT, 5, 1, 0, 0)
    elif Direction is 0:
        lj.AddRequest(device.lngHandle, lj.LJ_ioPUT_DIGITAL_BIT, 5, 0, 0, 0)
    lj.GoOne(device.lngHandle)

def deviceEmergency(emergency):
    lj.ePut (lj.lngHandle, lj.LJ_ioPUT_ANALOG_ENABLE_BIT, 4, 0, 0)
    if emergency is True:
        lj.AddRequest(device.lngHandle, lj.LJ_ioPUT_DIGITAL_BIT, 5, 0, 0, 0)
        lj.AddRequest(device.lngHandle, lj.LJ_ioPUT_DIGITAL_BIT, 6, 0, 0, 0)
    elif emergency is False:
        lj.AddRequest(device.lngHandle, lj.LJ_ioPUT_DIGITAL_BIT, 5, 1, 0, 0)
        lj.AddRequest(device.lngHandle, lj.LJ_ioPUT_DIGITAL_BIT, 6, 1, 0, 0)
    lj.GoOne(device.lngHandle)

def deviceEnable(detection):
    lj.ePut (device.lngHandle, lj.LJ_ioPUT_ANALOG_ENABLE_BIT, 6, 0, 0)
    if detection is True:
        lj.AddRequest(device.lngHandle, lj.LJ_ioPUT_DIGITAL_BIT, 6, 1, 0, 0)
    elif detection is False:
        lj.AddRequest(device.lngHandle, lj.LJ_ioPUT_DIGITAL_BIT, 6, 0, 0, 0)
    lj.GoOne(device.lngHandle)

def devicePower(enable):
    lj.ePut (device.lngHandle, lj.LJ_ioPUT_ANALOG_ENABLE_BIT, 3, 0, 0)
    if enable is True:
        lj.AddRequest(device.lngHandle, lj.LJ_ioPUT_DIGITAL_BIT, 3, 1, 0, 0)
    if enable is False:
        deviceStartConifg()
        lj.AddRequest(device.lngHandle, lj.LJ_ioPUT_DIGITAL_BIT, 3, 0, 0, 0)


def deviceRamp():
    lj.ePut (device.lngHandle, lj.LJ_ioPUT_ANALOG_ENABLE_BIT, 13, 1, 0)
    lj.AddRequest(device.lngHandle, lj.LJ_ioPUT_AIN_RANGE, 13, lj.LJ_rgBIP5V, 0, 0)
    lj.GoOne(device.lngHandle)