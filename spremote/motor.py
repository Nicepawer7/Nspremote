import time

from . import logger

class Motor:
    ''' A motor connected to a hub block. '''
    
    def __init__(self, hub):
        '''
        Prepare hub for motor usage and set motor settings.
    
        :param Hub hub: [](#Hub) object the motor is connected to.
        :param str port:  Identifier of the hub port the sensor is connected to
                          (one of `'A'`, `'B'`, `'C'`, `'D'`, `'E'`, `'F'`).
        :param bool lock: Hold position (`True`) or don't lock position
                          (`False`).
        :param float speed: Default speed in percent of maximum speed.
        :param float acc: Default acceleration in percent of maximum
                          acceleration.
        :param float dec: Default deceleration in percent of maximum
                          deceleration.
        '''

        self.hub = hub
        self.hub.cmd('from spike import Motor')
        # relative to absolute
        
        # stop and (un)lock motor
 

    def start(self,porta,speed = 50):
        '''
        Start the motor.
        
        :param float speed: Speed in percent of maximum speed (sign is direction
               of rotation). If `None`, default speed is used.
        :param float acc: Acceleration in percent of maximum acceleration. If
                          `None`, default acceleration is used.
        '''
        

        if porta == "'A'":
            self.hub.cmd(f'Motor({porta}).start({-speed})')
        elif porta == "'B'":
            self.hub.cmd(f'Motor({porta}).start({speed})')


        

    def stop(self,porta):
        '''
        Stop the motor by turning off power (no controlled deceleration).
        
        Until speed is 0 the locking flag corresponds to braking.
        
        :param bool lock: Lock position after stopping? If `None`, default
                          behavior is used.
        '''
        
        
        
        self.hub.cmd(f'Motor({porta}).stop()')        
     
    def run_degrees(self,porta, degrees, speed=50):      

        self.hub.cmd(f'motor({porta}).run_for_degrees({int(degrees)},{int(speed)}')


    def get_position(self,porta):
        '''
        Read current position in degrees.
        
        :return int: Current position in degrees.
        '''
        
        gradi_percorsi = self.hub.cmd(f'Motor({porta}).get_degrees_counted()')



        return int(gradi_percorsi)
    