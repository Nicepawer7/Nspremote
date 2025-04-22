# Load the gamepad and time libraries
import Gamepad.Gamepad
from time import sleep

class Input:
    def __init__(self,controller):
        self.g = Gamepad.Gamepad
        print('Waiting for gamepad')
        i = 0
        while not self.g.available() and i < 30:
            sleep(1)
            i += 1
            print(i)
        if self.g.available():
            print("Gamepad connesso")
            if controller == "PS3":
                gamepadType = self.g.PS3
            elif controller == "PS4":
                gamepadType = self.g.PS4
            elif controller == "Xbox360":
                gamepadType = self.g.Xbox360
            elif controller == "XboxONE":
                gamepadType = self.g.XboxONE
            elif controller == "Steam":
                gamepadType = self.g.Steam
            elif controller == "MMP1251":
                gamepadType = self.g.MMP1251

            elif controller == "PG9099":
                gamepadType = self.g.PG9099
            self.gamepad = gamepadType()
            self.gamepad.startBackgroundUpdates()
            pass
        
    def arduino_map(self,x,in_min,in_max,out_min,out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def right_speed(self):
        r_speed = ((self.gamepad.axis('R2')+1)/2)*100
        if r_speed > 5:
            return self.arduino_map(r_speed,0,100,25,100)
        else:
            return 0      
    
    def left_speed(self):
        l_speed = ((self.gamepad.axis('L2')+1)/2)*100
        if l_speed > 5:
            return self.arduino_map(l_speed,0,100,25,100)
        else:
            return 0
    def input_speed(self):
        pressed = {
            'r2':self.right_speed(),
            'l2':self.left_speed(),
            'r3y':-(self.gamepad.axis('RIGHT-Y'))*100,
            'l3y':-(self.gamepad.axis('LEFT-Y'))*100
        }
        return pressed
    def is_pressed(self):
        pressed = {
        'cross':self.gamepad.beenPressed('CROSS'),
        'circle':self.gamepad.beenPressed('CIRCLE'),
        'square':self.gamepad.beenPressed('SQUARE'),
        'triangle':self.gamepad.beenPressed('TRIANGLE'),
        'l1':self.gamepad.isPressed('L1'),
        'r1':self.gamepad.isPressed('R1'),
        }
        return pressed
    def disconnect(self):
        self.gamepad.disconnect()
    
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



