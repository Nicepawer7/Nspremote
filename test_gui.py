import tkinter as tk
from tkinter import ttk
from time import sleep
from time import time
import threading
import controll
import random
#pair = spremote.MotorPair(hub, 'A','B')

class MainApplication():
    speed = 0
    def __init__(self,w,h,title):
        #init window
        self.root = tk.Tk()
        self.root.geometry(f'{w}x{h}')
        self.root.minsize(w,h)
        self.root.maxsize(w,h)
        self.root.title(title)
        self.binding = Binding()
        #create,place and bind to situations widgets
        self.stop = False
        self.controller_init = threading.Thread(target=self.controller,daemon=True)
        self.l_speed= 0
        self.create_widget()
        self.place_widget()
        self.bind_buttons()
        # start thread to read and update giroscope telemetry without stopping main thread
        telemetry = threading.Thread(target=self.get_telemetry,daemon=True)
        telemetry.start()
        self.root.mainloop()
        self.stop = True
        self.pad.disconnect()

    def create_widget(self): #create widget
        #movement buttons
        self.forward = tk.Button(self.root,text ="▲",height=2,width=10)
        self.backward = tk.Button(self.root,text = "▼",height=2,width=10)
        self.sinistro = tk.Button(self.root,text="◀",height=2,width=10)
        self.destro = tk.Button(self.root,text="▶",height=2,width=10)
        self.both_destro = tk.Button(self.root,text="↷")
        self.both_sinistro = tk.Button(self.root,text="↶")
        #arms motors controll
        self.braccio_sinistro_avanti = tk.Button(self.root,text="▼",height=4,width=3)
        self.braccio_sinistro_indietro = tk.Button(self.root,text="▲",height=4,width=3)
        self.braccio_destro_avanti = tk.Button(self.root,text="▼",height=4,width=3)
        self.braccio_destro_indietro = tk.Button(self.root,text="▲",height=4,width=3)
        #connect controller?
        self.connect = tk.Button(self.root,text="Connect Controller",command=self.controller_init.start)
        #telemetry labels
        self.yaw_text = tk.Label(self.root, text="YAW: ")
        self.yaw_print = tk.Label(self.root, text=0)
        self.roll_text = tk.Label(self.root, text="ROLL: ")
        self.roll_print = tk.Label(self.root, text=0)
        self.pitch_text = tk.Label(self.root, text="PITCH: ")
        self.pitch_print = tk.Label(self.root, text=0)
        self.port_a_text = tk.Label(self.root, text="PORTA A: ")
        self.port_a_label = tk.Label(self.root, text=0)
        self.port_c_text = tk.Label(self.root, text="PORTA C: ")
        self.port_c_label = tk.Label(self.root, text=0)
        self.port_e_text = tk.Label(self.root, text="PORTA E: ")
        self.port_e_label = tk.Label(self.root, text=0)
        self.port_b_text = tk.Label(self.root, text="PORTA B: ")
        self.port_b_label = tk.Label(self.root, text=0)
        self.port_d_text = tk.Label(self.root, text="PORTA D: ")
        self.port_d_label = tk.Label(self.root, text=0)
        self.port_f_text = tk.Label(self.root, text="PORTA F: ")
        self.port_f_label = tk.Label(self.root, text=0)
        self.speed_text = tk.Label(self.root,text="Velocità di movimento:")
        self.speed_print = tk.Label(self.root,text=0)
        #speeds scales
        self.movement_speed_scale = ttk.Scale(self.root,from_=0,to=100,length=250,)
        self.velocità_braccio_sinistro = ttk.Scale(self.root,from_=100,to=0,length=200,orient=tk.VERTICAL)
        self.velocità_braccio_destro = ttk.Scale(self.root,from_=100,to=0,length=200,orient=tk.VERTICAL)

    def place_widget(self): # place widget
        #movement buttons
        self.forward.place(x=250,y=165,anchor=tk.S)
        self.backward.place(x=250,y=225,anchor=tk.N)
        self.sinistro.place(x=250,y=195,anchor=tk.E)
        self.destro.place(x=250,y=195,anchor=tk.W)
        self.both_sinistro.place(x=175,y=152,anchor=tk.SE)
        self.both_destro.place(x=325,y=152,anchor=tk.SW)
        #speed scale
        self.movement_speed_scale.place(x = 250,y = 325,anchor=tk.CENTER)
        self.velocità_braccio_destro.place(x=470,y=205,anchor=tk.CENTER)
        self.velocità_braccio_sinistro.place(x=30,y=205,anchor=tk.CENTER)
        # arms
        self.braccio_destro_avanti.place(x=420,y=315,anchor=tk.S)
        self.braccio_sinistro_avanti.place(x=80,y=315,anchor=tk.S)
        self.braccio_destro_indietro.place(x=420,y=95,anchor=tk.N)
        self.braccio_sinistro_indietro.place(x=80,y=95,anchor=tk.N)
        # connect controller
        self.connect.place(x=250,y=360,anchor=tk.CENTER)
        #labels gyro + speed
        self.speed_text.place(x=235,y=300,anchor=tk.CENTER)
        self.yaw_text.place(x=75,y=25,anchor=tk.CENTER)
        self.roll_text.place(x=75,y=50,anchor=tk.CENTER)
        self.pitch_text.place(x=75,y=75,anchor=tk.CENTER)
        #port labels
        self.port_a_text.place(x=275,y=25,anchor=tk.E)
        self.port_c_text.place(x=275,y=50,anchor=tk.E)
        self.port_e_text.place(x=275,y=75,anchor=tk.E)
        self.port_b_text.place(x=395,y=25,anchor=tk.CENTER)
        self.port_d_text.place(x=395,y=50,anchor=tk.CENTER)
        self.port_f_text.place(x=395,y=75,anchor=tk.CENTER)  
        #port dynamic labels
        self.port_a_label.place(x=275,y=25,anchor=tk.W)
        self.port_c_label.place(x=275,y=50,anchor=tk.W)
        self.port_e_label.place(x=275,y=75,anchor=tk.W)
        self.port_b_label.place(x=435,y=25,anchor=tk.W)
        self.port_d_label.place(x=435,y=50,anchor=tk.W)
        self.port_f_label.place(x=435,y=75,anchor=tk.W)
        #gyro + speed dynamic labels
        self.yaw_print.place(x=100,y=25,anchor=tk.W)
        self.roll_print.place(x=100,y=50,anchor=tk.W)
        self.pitch_print.place(x=100,y=75,anchor=tk.W)
        self.speed_print.place(x=330,y=300,anchor=tk.W)

    def bind_buttons(self):
        #press
        #motori pair
        self.backward.bind('<ButtonPress-1>',self.binding.indietro)
        self.forward.bind('<ButtonPress-1>',self.binding.avanti)
        self.both_destro.bind('<ButtonPress-1>',lambda event: self.binding.spot_turn("destra"))
        self.both_sinistro.bind('<ButtonPress-1>',lambda event: self.binding.spot_turn("sinistra"))
        #motori singoli
        self.sinistro.bind('<ButtonPress-1>',lambda event: self.binding.gira_motore("'A'",-1))
        self.destro.bind('<ButtonPress-1>',lambda event: self.binding.gira_motore("'B'"))
        self.braccio_sinistro_avanti.bind('<ButtonPress-1>',lambda event: self.binding.gira_motore("'C'"))
        self.braccio_sinistro_indietro.bind('<ButtonPress-1>',lambda event: self.binding.gira_motore("'C'",-1))
        self.braccio_destro_avanti.bind('<ButtonPress-1>',lambda event: self.binding.gira_motore("'D'"))  
        self.braccio_destro_indietro.bind('<ButtonPress-1>',lambda event: self.binding.gira_motore("'D'",-1))
        #release
        #pair 
        self.backward.bind('<ButtonRelease-1>',self.binding.stop_pair)
        self.forward.bind('<ButtonRelease-1>',self.binding.stop_pair)
        self.both_destro.bind('<ButtonRelease-1>',self.binding.stop_pair)
        self.both_sinistro.bind('<ButtonRelease-1>',self.binding.stop_pair)
        # motori singoli
        self.sinistro.bind('<ButtonRelease-1>',lambda event: self.binding.stop_motor("'A'"))
        self.destro.bind('<ButtonRelease-1>',lambda event:self.binding.stop_motor("'B'"))
        self.braccio_sinistro_avanti.bind('<ButtonRelease-1>',lambda event:self.binding.stop_motor("'C'"))
        self.braccio_sinistro_indietro.bind('<ButtonRelease-1>',lambda event:self.binding.stop_motor("'C'"))
        self.braccio_destro_avanti.bind('<ButtonRelease-1>',lambda event:self.binding.stop_motor("'D'"))
        self.braccio_destro_indietro.bind('<ButtonRelease-1>',lambda event:self.binding.stop_motor("'D'"))   

    def get_telemetry(self):
        tstart = time()
        while True:
            self.movement_speed = int(self.movement_speed_scale.get())
            yaw_value = int(random.uniform(-180,180))
            roll_value = int(random.uniform(-180,180))
            pitch_value = int(random.uniform(-180,180))
            A_value = int(random.uniform(-180,180))
            B_value = int(random.uniform(-180,180))
            C_value = int(random.uniform(-180,180))
            D_value = int(random.uniform(-180,180))
            E_value = int(random.uniform(-180,180))
            F_value = int(random.uniform(-180,180))

            if time() - tstart >= 0.5:
                tstart = time()
                self.yaw_print.config(text=yaw_value)
                self.roll_print.config(text=pitch_value)
                self.pitch_print.config(text=roll_value)
                self.port_a_label.config(text=A_value)
                self.port_b_label.config(text=B_value)
                self.port_c_label.config(text=C_value)
                self.port_d_label.config(text=D_value)
                self.port_e_label.config(text=E_value)
                self.port_f_label.config(text=F_value)
            self.speed_print.config(text=self.movement_speed)
    def controller(self):
        self.pad = controll.Input()
        l_running = False
        r_running = False
        while True:
            sleep(10)
            while not self.stop and self.pad.g.available():
                speed = self.pad.input_speed()
                if speed["l2"] > 20:
                    self.binding.gira_motore('A',velocità=speed["l2"])
                    l_running = True
                elif l_running == True and speed["l2"] < 20:
                    self.binding.stop_motor('A')
                    l_running = False
                if speed["r2"] > 20:
                    self.binding.gira_motore('B',velocità=speed["r2"])
                    r_running = True
                elif r_running == True and speed["r2"] < 20:
                    self.binding.stop_motor('B')
                    print("Motore fermato")
                    r_running = False
                pressed = self.pad.is_pressed()
                print(pressed["cross"])
                self.speed_print.configure(text=max(speed["l2"],speed["r2"]))
                self.movement_speed_scale.set(max(speed["l2"],speed["r2"]))
                sleep(0.1)

            print("Controller not found,waiting")

class Binding():
    def avanti(self,event):
        print("Coppia motore partita avanti a velocità")
    def indietro(self,event):
        print("Coppia motore partita indietro a velocità")
    def gira_motore(self,porta,direzione = 1,velocità = 50):
        print("Avviato motore " + porta + " in direzione " + str(direzione) + " a velocità" + str(velocità))
    def stop_pair(self,event):
        print("Fermata coppia motori")
    def stop_motor(self,porta):
        print("Fermato motore singolo " + str(porta))
    def spot_turn(self,direzione):
        print("Giro sul posto")
        #pair.turn_on_spot(direzione)

MainApplication(500,385,"NSPremote")   
