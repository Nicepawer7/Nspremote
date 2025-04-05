from tkinter import * 
import spremote
from time import sleep

hub = spremote.Hub('/dev/ttyACM1')
lb = spremote.Button(hub, 'LEFT')
rb = spremote.Button(hub, 'RIGHT')
pair = spremote.MotorPair(hub, 'A','B')
speed = 50#int(input())



root = Tk()
def avanti(event):
    pair.start(speed)
def indietro(event):
    pair.start(-speed)
def gira_Sinistro(event):
    spremote.Motor(hub).start("'B'")
def gira_Destro(event):
    spremote.Motor(hub).start("'A'")
def stop_pair(event):
    pair.stop()
def stop_motor(porta):
    spremote.Motor(hub).stop(porta)

forward = Button(root, text ="↑")
backward = Button(root,text = "↓")
sinistro = Button(root,text="<")
destro = Button(root,text="→")
forward.pack(side=TOP)
backward.pack(side=BOTTOM)
sinistro.pack(side=LEFT)
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