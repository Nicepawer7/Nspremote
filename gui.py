from tkinter import * 
import spremote
from time import sleep

#hub = spremote.Hub('/dev/ttyACM0')
hub = spremote.Hub('/dev/rfcomm1')
lb = spremote.Button(hub, 'LEFT')
rb = spremote.Button(hub, 'RIGHT')
pair = spremote.MotorPair(hub, 'A','B')
speed = 70#int(input())
motion = spremote.MotionSensor(hub)



root = Tk()
def avanti(event):
    pair.start(speed)
def indietro(event):
    pair.start(-speed)
def gira_Sinistro(event):
    spremote.Motor(hub).start("'B'",speed=70)
def gira_Destro(event):
    spremote.Motor(hub).start("'A'",speed=70)
def stop_pair(event):
    pair.stop()
def stop_motor(porta):
    spremote.Motor(hub).stop(porta)

forward = Button(root, text ="↑")
backward = Button(root,text = "↓")
sinistro = Button(root,text="←")
both_destro = Button(root,text="↷").pack()
destro = Button(root,text="→")
both_sinistro = Button(root,text="↶").pack()
yaw = Label(root, text=motion.get_yaw()).pack() 
forward.pack(side=TOP)
backward.pack(side=BOTTOM)
sinistro.pack(side=LEFT)
#both_sinistro.grid(row=2,column=1)
destro.pack(side=RIGHT)
backward.bind('<ButtonPress-1>',indietro)
backward.bind('<ButtonRelease-1>',stop_pair)
forward.bind('<ButtonPress-1>',avanti)
forward.bind('<ButtonRelease-1>',stop_pair)
sinistro.bind('<ButtonPress-1>',gira_Sinistro)
sinistro.bind('<ButtonRelease-1>',lambda event: stop_motor("'B'"))
destro.bind('<ButtonPress-1>',gira_Destro)
destro.bind('<ButtonRelease-1>',lambda event:stop_motor("'A'"))
root.mainloop()
