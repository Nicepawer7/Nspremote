# Load the gamepad and time libraries
import Gamepad.Gamepad
from time import sleep

g = Gamepad.Gamepad
gamepadType = g.PS4




gamepad = gamepadType()
print('Gamepad connected')

gamepad.startBackgroundUpdates()

class Input:
    def __init__(self):
        if not g.available():
            i = 0
            print('Waiting for gamepad')
            while not g.available() or i < 30:
                sleep(1)
                i += 1
    def arduino_map(self,x,in_min,in_max,out_min,out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def right_speed(self):
        r_speed = ((gamepad.axis('R2')+1)/2)*100
        if r_speed > 5:
            return self.arduino_map(r_speed,0,100,25,100)
        else:
            return 0      
    
    def left_speed(self):
        l_speed = ((gamepad.axis('L2')+1)/2)*100
        if l_speed > 5:
            return self.arduino_map(l_speed,0,100,25,100)
        else:
            return 0

    def disconnect():
        gamepad.disconnect()
    
    """# Check for happy button changes
        if gamepad.beenPressed('PS'):
            print("BOOOOOOOOOOOOM")
            break
        if gamepad.beenPressed('CROSS'):
            print(':)')
        if gamepad.beenReleased('CIRCLE'):
            print(':(')

        if gamepad.isPressed('SQUARE'):
            print('BEEP')"""



