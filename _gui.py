import spremote
from time import sleep
speed  = 70
#hub = spremote.Hub('/dev/ttyACM0')
hub = spremote.Hub('/dev/rfcomm0')
pair = spremote.MotorPair(hub, 'A','B')
motion = spremote.MotionSensor(hub)

def avanti(event):
    pair.start(speed)
def indietro(event):
    pair.start(-speed)
def gira_motore(porta,direzione = 1):
    spremote.Motor(hub).start(porta,speed=70,direzione=direzione)
def stop_pair(event):
    pair.stop()
def stop_motor(porta):
    spremote.Motor(hub).stop(porta)

