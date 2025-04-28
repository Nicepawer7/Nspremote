class MotionSensor:
    ''' Motion sensor integrated into a hub block. '''
        
    def __init__(self, hub):
        '''
        Prepare hub for using the motion sensor.
    
        :param Hub hub: [](#Hub) object the motion sensor belongs to.
        :param str up: Side of hub block facing upwards (used for relative angle
                       measurements, see [](#reset) for details).
        '''
        
        self.hub = hub
        self.hub.cmd('from spike import motion_sensor')
        self.reset()
        
    
    def reset(self):
        self.hub.cmd(f'motion_sensor.reset_yaw_angle()')

    def get_angular_velocity(self):
        '''
        Read angular velocity.
        
        For interpretation of angles take the coordinate system y, p, r defined
        in [](#get_orientation) for buttons side facing upwards. Angular
        velocities are positive if angles described there increase.
        
        :return (float, float, float): Angular velocity for rotation around axes
                                       r, p, y in degrees per second.
        '''
        
        ret = self.hub.cmd(f'motion_sensor.angular_velocity(True)')     
        print("da testare")  
        return tuple(int(x) / 10 for x in ret[-1][1:-1].split(','))


    def get_acceleration(self):
        '''
        Read acceleration.

        For interpretation of accelerations take the coordinate system y, p, r
        defined in [](#get_orientation) for buttons side facing upwards.
        Accelerations are positive in direction of the axes.
        
        :return (float, float, float): Acceleration in r, p, y direction in G.
                                       Note that even if the hub doesn't move,
                                       values aren't all zero due to
                                       gravitation.
        '''
        
        ret = self.hub.cmd(f'motion_sensor.acceleration(True)') 
        print("da testare")       
        return tuple(int(x) / 1000 for x in ret[-1][1:-1].split(','))
    
    def get_yaw(self):
        ret = self.hub.cmd(f'PrimeHub().motion_sensor.get_yaw_angle()')
        return ret
    
    def get_pitch(self):
        ret = self.hub.cmd(f'PrimeHub().motion_sensor.get_pitch_angle()')
        return ret
    
    def get_roll(self):
      ret = self.hub.cmd(f'PrimeHub().motion_sensor.get_roll_angle()')
      return ret
        

