#STD Python Librayies
from tkinter import *
from threading import Thread

#Personal Python Libraries
import application as app
import excecute as exe

global root
root = Tk()

global sp,or_,dr
sp = or_ = dr = 0

def loop():
    exe.motorDirection(0)
    exe.getCur()
    exe.reset(0)
    exe.EMERGENCY(1)

def main():
    root.geometry("350x150")
    #Threading Proccesses
    thread = Thread(target=loop())
    thread.start()

    #Labels
    onRamp_lbl()
    speed_lbl()
    downRamp_lbl()
    current_motor()
    current_measure()
    
    #Buttons
    clockwise("active")
    counterClockwise("active")
    start("start","active")

    #Run GUI
    root.mainloop()

def current_measure():
    current = Label(root,text=str(app.getCurrent()))
    current.grid()
    current.place(x=215,y=130)

def current_motor():
    current = Label(root,text="Motor Current: ")
    current.grid()
    current.place(x=125,y=130)

def onRamp_lbl():
    onramp_lbl = Label(root,text="ON Ramp(ms)")
    onramp_lbl.grid()
    onramp_lbl.place(x=25,y=10)

def speed_lbl():
    speedlbl = Label(root,text="Speed(%)")
    speedlbl.grid()
    speedlbl.place(x=125,y=10)

def downRamp_lbl():
    downramplbl = Label(root,text="DOWN Ramp(ms)")
    downramplbl.grid()
    downramplbl.place(x=225,y=10)

def clockwise(state_):
    direction = 1
    cw = Button(root, text="Clockwise",command=app.startMotor(),state=state_)
    cw.grid()
    cw.place(x=25,y=70,width=150)

def counterClockwise(state_):
    direction = -1
    ccw = Button(root, text="Counter Clockwise",command=app.motorRotation(direction),state=state_)
    ccw.grid()
    ccw.place(x=175,y=70,width=150)

def start(value,state_):
    s = Button(root, text=value,command=app.start_motor(),state=state_)
    s.grid()
    s.place(x=25,y=100, width=300)

def onRamp(val):
    or_ = Scale(root, from_=10, to=1000,orient=HORIZONTAL)
    or_.grid()
    or_.get()
    or_.place(x=25,y=30)
    or_.set(val)

def speed(val):
    sp = Scale(root, from_=0, to=100,orient=HORIZONTAL)
    sp.grid()
    sp.get()
    sp.place(x=125,y=30)
    sp.set(val)

def downRamp(val):
    dr = Scale(root, from_=10, to=1000,orient=HORIZONTAL)
    dr.grid()
    dr.get()
    dr.place(x=225,y=30)
    dr.set(val)

def changeSpeed(opt):    # initializing dutyCycle for slope
    if(opt == -1 ):                         #Calculate downramp speed
        dutyCycle.set(dutyCycle.get() -(sp.get()/dnRampScale.get()))
    else:                                   #Calculate upramp speed
       dutyCycle.set(dutyCycle.get() + (speedScale.get()/upRampScale.get()))
    print("Duty Cycle: ", dutyCycle.get(), " %")
    


if __name__ == "__main__":
    main()