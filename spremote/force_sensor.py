class ForceSensor:
    ''' A force sensor connected to a hub block. '''
    
    def __init__(self,hub,port):
        '''
        Prepare hub for usage of a force sensor.
    
        :param Hub hub: [](#Hub) object the force sensor is connected to.
        :param str port:  Identifier of the hub port the sensor is connected to
                          (one of `'A'`, `'B'`, `'C'`, `'D'`, `'E'`, `'F'`).
        '''
        self.hub = hub
        self.hub.cmd('from spike import ForceSensor')
        self.port = "ForceSensor('" + port + "')"
        print(self.port)
        
        
    def is_pressed(self):
        '''
        get's force in newton
    
        :return int: ForNewtons read from sensor.
        '''
        
        ret = self.hub.cmd(f'{self.port}.is_pressed()')
        
        return int(ret)
    
    def get_force_newton(self):
        '''
        get's force in newton
    
        :return int: ForNewtons read from sensor.
        '''
        
        ret = self.hub.cmd(f'{self.port}.get_force_newton()')
        
        return int(ret)
    
    def get_force_percentage(self):
        '''
        get's force in newton
    
        :return int: ForNewtons read from sensor.
        '''
        
        ret = self.hub.cmd(f'{self.port}.get_force_percentage()')
        
        return int(ret)
