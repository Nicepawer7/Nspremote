class DistanceSensor:
    ''' A distance sensor connected to a hub block. '''
    
    def __init__(self, hub, port):
        '''
        Prepare hub for usage of a color sensor.
    
        :param Hub hub: [](#Hub) object the color sensor is connected to.
        :param str port:
        '''
        
        self.hub = hub
        self.hub.cmd('from spike import DistanceSensor')
        self.port = "DistanceSensor('" + port + "')"
        self.light_up_all()
        
    
    def light_up_all(self,brightness = 100):
        '''
        Turn all lights of the sensor on.
        '''     
        self.hub.cmd(f'{self.port}.light_up_all({brightness})')       

    def light_up(self,right_top = 100, left_top = 100, right_bottom = 100, left_bottom = 100):
        '''
        Turn single lights on
        :right_top = 0 - 100
        :left_top = 0 - 100
        :right_bottom = 0 - 100
        :lft_bottom = 0 - 100
        '''     
        lights = []
        lights[0] = right_top
        lights[1] = left_top
        lights[2] = right_bottom
        lights[3] = left_bottom
        i = 0
        while i < 4:
            if lights[i] > 100:
                lights[i] = 100
            elif lights[i] < 0:
                lights[i] = 0
            i += 1
        self.hub.cmd(f'{self.port}.light_up({right_top},{left_top},{right_bottom},{left_bottom})')       

    def get_distance_cm(self,short_range = False):
        '''
        Return distance in cm
        :param short_range for better measurement but close range
        :int distance
        '''    

        ret = self.hub.cmd(f'{self.port}.get_distance_cm(short_range = {short_range})')
        return ret

    def get_distance_inches(self,short_range = False):
        '''
        Return distance in inches
        :param short_range for better measurement but close range
        :int distance
        '''    

        ret = self.hub.cmd(f'{self.port}.get_distance_inches(short_range = {short_range})')
        return ret

    def get_distance_percentage(self,short_range = False):
        '''
        Return distance in percentage
        :param short_range for better measurement but close range
        :int distance 0-100
        '''    

        ret = self.hub.cmd(f'{self.port}.get_distance_percentage(short_range = {short_range})')
        return ret
