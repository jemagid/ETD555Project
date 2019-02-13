from tkinter import *
import application  as app

global root
root = Tk()

global sp,or_,dr
sp = or_ = dr = 0

def main():
    root.geometry("350x150")
    #Labels
    onRamp_lbl()
    speed_lbl()
    downRamp_lbl()
    mosfet_temp()
    temperature_measure()
    current_motor()
    current_measure()

    #Sliders
    onRamp()
    speed()
    downRamp()

    #Buttons
    clockwise()
    counterClockwise()
    start()

    #Run GUI
    root.mainloop()

def temperature_measure():
    tmp = Label(root,text=str(app.getTmp()))
    tmp.grid()
    tmp.place(x=115,y=130)

def current_measure():
    current = Label(root,text=str(app.getCurrent()))
    current.grid()
    current.place(x=215,y=130)

def mosfet_temp():
    tmp = Label(root,text="Mosfet Temp: ")
    tmp.grid()
    tmp.place(x=25,y=130)

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

def clockwise():
    cw = Button(root, text="Clockwise",COMMAND=app.clockwise_Rotation())
    cw.grid()
    cw.place(x=25,y=70,width=150)

def counterClockwise():
    ccw = Button(root, text="Counter Clockwise",COMMAND=app.counter_clockwise_Rotation())
    ccw.grid()
    ccw.place(x=175,y=70,width=150)

def start():
    s = Button(root, text="Start",COMMAND=app.start_motor())
    s.grid()
    s.place(x=25,y=100, width=300)

def onRamp():
    or_ = Scale(root, from_=10, to=1000,orient=HORIZONTAL)
    or_.grid()
    or_.get()
    or_.place(x=25,y=30)

def speed():
    sp = Scale(root, from_=0, to=100,orient=HORIZONTAL)
    sp.grid()
    sp.get()
    sp.place(x=125,y=30)

def downRamp():
    dr = Scale(root, from_=10, to=1000,orient=HORIZONTAL)
    dr.grid()
    dr.get()
    dr.place(x=225,y=30)

def getUp():
    return or_

def getDown():
    return dr

def getSpeed():
    return sp

if __name__ == "__main__":
    main()