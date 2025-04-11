from tkinter import * 
from time import sleep
#tk init
root = Tk()
root.geometry("1000x600")
root.title("NiceControll")
speed = 70#int(input())
# onfiguta griglia


def avanti(event):
    print("Coppia motore partita avanti")
def indietro(event):
    print("Coppia motore partita indietro")
def gira_Sinistro(event):
    print("Avviato motore destro")
def gira_Destro(event):
    print("Avviato motore sinistro")
def stop_pair(event):
    print("Fermata coppia motori")
def stop_motor(porta):
    print("Fermto motore singolo")

forward = Button(root, text ="↑",height=2,width=10)
backward = Button(root,text = "↓",height=2,width=10)
sinistro = Button(root,text="←",height=2,width=10)
destro = Button(root,text="→",height=2,width=10)
both_destro = Button(root,text="↷")
both_sinistro = Button(root,text="↶")
yaw = Label(root, text="0")
#positions
forward.place(x=500,y=270,anchor=S)
backward.place(x=500,y=330,anchor=N)
sinistro.place(x=500,y=300,anchor=E)
destro.place(x=500,y=300,anchor=W)
both_sinistro.place(x=430,y=260,anchor=SE)
both_destro.place(x=400,y=600,anchor=SW)
yaw.place(x=800,y=600,anchor=CENTER)

#bind
backward.bind('<ButtonPress-1>',indietro)
backward.bind('<ButtonRelease-1>',stop_pair)
forward.bind('<ButtonPress-1>',avanti)
forward.bind('<ButtonRelease-1>',stop_pair)
sinistro.bind('<ButtonPress-1>',gira_Sinistro)
sinistro.bind('<ButtonRelease-1>',lambda event: stop_motor("'B'"))
destro.bind('<ButtonPress-1>',gira_Destro)
destro.bind('<ButtonRelease-1>',lambda event:stop_motor("'A'"))
root.mainloop()


"""
gyro = 0
yaw = Label(root,text="Yaw:").pack()
gyro_value = Label(root,text="yaw")
gyro_value.pack()
def giorscopio():
    gyro = int(random.uniform(-180,180))
    gyro_value.config(text=gyro)
    root.after(500,giorscopio)
root.after(500,giorscopio)
root.mainloop()"""