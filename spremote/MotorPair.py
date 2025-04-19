from time import sleep


class MotorPair:
    ''' A motor connected to a hub block. '''
    
    def __init__(self, hub, port1,port2, lock=False, speed=50, acc=100, dec=100):
        '''
        Prepare hub for motor usage and set motor settings.
    
        :param Hub hub: [](#Hub) object the force sensor is connected to.
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
        self.hub.cmd('from spike import MotorPair')
        self.port1 = f"'{port1}'"
        self.port2 = f"'{port2}'"
        
        # relative to absolute
        self.speed = int(speed / 100*100)
        self.acc = int(acc / 100 * 10000)
        self.dec = int(dec / 100 * 10000)
        
        # stop and (un)lock motor
        self.lock = lock
        self.hub.cmd(f'coppia = MotorPair({self.port1},{self.port2})')
        self.start(speed=0, acc=0)
        self.stop()
 

    def start(self, speed=None, acc=None):
        '''
        Start the motor.
        
        :param float speed: Speed in percent of maximum speed (sign is direction
               of rotation). If `None`, default speed is used.
        :param float acc: Acceleration in percent of maximum acceleration. If
                          `None`, default acceleration is used.
        '''
        
        if speed:
            speed = int(speed / 100 * 100)
        else:
            speed = self.speed
        if acc:
            acc = int(acc / 100 * 10000)
        else:
            acc = self.acc
        ret = self.hub.cmd(f'coppia.start_at_power({speed},0)')
        

    def stop(self, lock=None):
        '''
        Stop the motor by turning off power (no controlled deceleration).
        
        Until speed is 0 the locking flag corresponds to braking.
        
        :param bool lock: Lock position after stopping? If `None`, default
                          behavior is used.
        '''
        
        if lock == None:
            lock = self.lock
        
        ret = self.hub.cmd(f'coppia.stop()')
        
     
    def run_degrees(self, degrees, speed=None, acc=None, dec=None, lock=None, # non so se funziona alalalalala
                    wait=False):
        '''
        Run motor for number of degrees.
        
        Direction of rotation can be flipped via sign of `speed` or sign of
        `degrees`.
        
        :param float degrees: Number of degrees to run.
        :param float speed: Speed in percent of maximum speed. If `None`,
                            default speed is used.
        :param float acc: Acceleration in percent of maximum acceleration. If
                          `None`, default acceleration is used.
        :param float dec: Deceleration in percent of maximum deceleration. If
                          `None`, default deceleration is used.
        :param bool lock: Lock position after stopping? If `None`, default
                          behavior is used.
        :param book wait: Wait until motor has reached stop position or return
                          immediately?
        '''

        if speed:
            speed = int(speed / 100 * self.max_speed)
        else:
            speed = self.speed
        if acc:
            acc = int(acc / 100 * 10000)
        else:
            acc = self.dec
        if dec:
            dec = int(dec / 100 * 10000)
        else:
            dec = self.dec
        if degrees < 0:
            degrees = -degrees
            speed = -speed
        if lock == None:
            lock = self.lock

        ret = self.hub.cmd(
            f'coppia.run_for_degrees({int(degrees)}, {speed}, ' \
            f'acceleration={acc}, deceleration={dec}, stop={int(lock)})'
        )
        
        if wait:
            started = False
            stopped = False
            pos = self.get_position()  # -179...180
            end_pos = (pos + degrees % 360 + 180) % 360 - 180
            while not started or not stopped:
                prev_pos = pos
                pos = self.get_position()
                if pos != prev_pos and not started:
                    started = True
                if pos == prev_pos and abs(pos - end_pos) % 360 < 5 and started:
                    stopped = True
                sleep(0.1)


    def get_position(self):
        '''
        Read current position in degrees.
        
        :return int: Current position in degrees.
        '''
        
        ret = self.hub.cmd(f'motor.absolute_position({self.port1})')

        return int(ret[-1])
    def turn_on_spot(self,direzione,speed=70):
        
        match direzione:
            case 1:
                self.hub.cmd(f'coppia.start_tank_at_power({speed*-1},{speed})')
            case "sinistra":
                self.hub.cmd(f'coppia.start_tank_at_power({speed*-1},{speed})')
            case -1:
                self.hub.cmd(f'coppia.start_tank_at_power({speed},{speed*-1})')
            case "destra":
                self.hub.cmd(f'coppia.start_tank_at_power({speed},{speed*-1})')
        
   