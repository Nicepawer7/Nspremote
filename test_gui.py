import tkinter as tk
from tkinter import ttk
from time import sleep
import threading
import spremote
import random

#pair = spremote.MotorPair(hub, 'A','B')

class MainApplication():
    speed = 0
    def __init__(self,w,h,title):
        self.root = tk.Tk()
        self.root.geometry(f'{w}x{h}')
        self.root.minsize(w,h)
        self.root.title(title)
        self.create_widget()
        self.place_widget()
        self.bind_buttons()
        telemetry = threading.Thread(target=self.get_telemetry,daemon=True)
        telemetry.start()
        self.root.mainloop()

    def create_widget(self): #crea i bottoni e le etichette
        self.forward = tk.Button(self.root,text ="↑",height=2,width=10)
        self.backward = tk.Button(self.root,text = "↓",height=2,width=10)
        self.sinistro = tk.Button(self.root,text="↰",height=2,width=10)
        self.destro = tk.Button(self.root,text="↱",height=2,width=10)
        self.both_destro = tk.Button(self.root,text="↷")
        self.both_sinistro = tk.Button(self.root,text="↶")
        self.braccio_sinistro_avanti = tk.Button(self.root,text="<-",height=4,width=3)
        self.braccio_sinistro_indietro = tk.Button(self.root,text="->",height=4,width=3)
        self.braccio_destro_avanti = tk.Button(self.root,text="<-",height=4,width=3)
        self.braccio_destro_indietro = tk.Button(self.root,text="->",height=4,width=3)
        self.yaw_text = tk.Label(self.root, text="YAW: ")
        self.yaw_print = tk.Label(self.root, text=0)
        self.roll_text = tk.Label(self.root, text="ROLL: ")
        self.roll_print = tk.Label(self.root, text=0)
        self.pitch_text = tk.Label(self.root, text="PITCH: ")
        self.pitch_print = tk.Label(self.root, text=0)
        self.speed_text = tk.Label(self.root,text="Velocità")
        self.speed_print = tk.Label(self.root,text=0)
        self.movement_speed_scale = ttk.Scale(self.root,from_=0,to=100,length=250,)
        self.velocità_braccio_sinistro = ttk.Scale(self.root,from_=100,to=0,length=200,orient=tk.VERTICAL)
        self.velocità_braccio_destro = ttk.Scale(self.root,from_=100,to=0,length=200,orient=tk.VERTICAL)

    def place_widget(self): # li posiziona 
        self.forward.place(x=500,y=250,anchor=tk.S)
        self.backward.place(x=500,y=310,anchor=tk.N)
        self.sinistro.place(x=500,y=280,anchor=tk.E)
        self.destro.place(x=500,y=280,anchor=tk.W)
        self.both_sinistro.place(x=430,y=240,anchor=tk.SE)
        self.both_destro.place(x=570,y=240,anchor=tk.SW)
        self.movement_speed_scale.place(x = 500,y = 390,anchor=tk.CENTER)
        self.velocità_braccio_destro.place(x=275,y=300,anchor=tk.CENTER)
        self.velocità_braccio_sinistro.place(x=725,y=300,anchor=tk.CENTER)
        self.braccio_destro_avanti.place(x=675,y=305,anchor=tk.N)
        self.braccio_sinistro_avanti.place(x=325,y=305,anchor=tk.N)
        self.braccio_sinistro_indietro.place(x=325,y=295,anchor=tk.S)
        self.braccio_destro_indietro.place(x=675,y=295,anchor=tk.S)
        #self.yaw_text.place(x=400,y=400,anchor=tk.CENTER)
        self.yaw_print.place(x=400,y=500,anchor=tk.CENTER)
        #self.roll_text.place(x=400,y=550,anchor=tk.CENTER)
        self.roll_print.place(x=400,y=450,anchor=tk.CENTER)
        #self.pitch_text.place(x=400,y=200,anchor=tk.CENTER)
        self.pitch_print.place(x=400,y=100,anchor=tk.CENTER)
        self.speed_text.place(x=200,y=100,anchor=tk.CENTER)
        self.speed_print.place(x=300,y=100,anchor=tk.CENTER)

    def bind_buttons(self):
        binding = Binding()
        #press
        #motori pair
        self.backward.bind('<ButtonPress-1>',binding.indietro)
        self.forward.bind('<ButtonPress-1>',binding.avanti)
        self.both_destro.bind('<ButtonPress-1>',lambda event: binding.spot_turn("destra"))
        self.both_sinistro.bind('<ButtonPress-1>',lambda event: binding.spot_turn("sinistra"))
        #motori singoli
        self.sinistro.bind('<ButtonPress-1>',lambda event: binding.gira_motore("'A'"-1))
        self.destro.bind('<ButtonPress-1>',lambda event: binding.gira_motore("'B'"))
        self.braccio_sinistro_avanti.bind('<ButtonPress-1>',lambda event: binding.gira_motore("'C'"))
        self.braccio_sinistro_indietro.bind('<ButtonPress-1>',lambda event: binding.gira_motore("'C'",-1))
        self.braccio_destro_avanti.bind('<ButtonPress-1>',lambda event: binding.gira_motore("'D'"))  
        self.braccio_destro_indietro.bind('<ButtonPress-1>',lambda event: binding.gira_motore("'D'",-1))
        #release
        #pair 
        self.backward.bind('<ButtonRelease-1>',binding.stop_pair)
        self.forward.bind('<ButtonRelease-1>',binding.stop_pair)
        self.both_destro.bind('<ButtonRelease-1>',binding.stop_pair)
        self.both_sinistro.bind('<ButtonRelease-1>',binding.stop_pair)
        # motori singoli
        self.sinistro.bind('<ButtonRelease-1>',lambda event: binding.stop_motor("'A'"))
        self.destro.bind('<ButtonRelease-1>',lambda event:binding.stop_motor("'B'"))
        self.braccio_sinistro_avanti.bind('<ButtonRelease-1>',lambda event:binding.stop_motor("'C'"))
        self.braccio_sinistro_indietro.bind('<ButtonRelease-1>',lambda event:binding.stop_motor("'C'"))
        self.braccio_destro_avanti.bind('<ButtonRelease-1>',lambda event:binding.stop_motor("'D'"))
        self.braccio_destro_indietro.bind('<ButtonRelease-1>',lambda event:binding.stop_motor("'D'"))   

    def get_telemetry(self):
        while True:
            self.movement_speed = int(self.movement_speed_scale.get())
            yaw_value = int(random.uniform(-180,180))
            roll_value = int(random.uniform(-180,180))
            pitch_value = int(random.uniform(-180,180))
            self.yaw_print.config(text=yaw_value)
            self.roll_print.config(text=pitch_value)
            self.pitch_print.config(text=roll_value)
            self.speed_print.config(text=self.movement_speed)
            sleep(0.5)

class Binding():
    def avanti(self,event):
        print("Coppia motore partita avanti a velocità")
    def indietro(self,event):
        print("Coppia motore partita indietro a velocità")
    def gira_motore(self,porta,direzione = 1):
        print("Avviato motore " + porta + "in direzione " + str(direzione))
    def stop_pair(self,event):
        print("Fermata coppia motori")
    def stop_motor(self,porta):
        print("Fermto motore singolo")
    def spot_turn(self,direzione):
        print("Giro sul posto")
        #pair.turn_on_spot(direzione)

MainApplication(1000,600,"NSPremote")   