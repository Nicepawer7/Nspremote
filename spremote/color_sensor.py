class ColorSensor:
    ''' A color sensor connected to a hub block. '''
    
    def __init__(self, hub, port):
        '''
        Prepare hub for usage of a color sensor.
    
        :param Hub hub: [](#Hub) object the color sensor is connected to.
        :param str port:  Identifier of the hub port the sensor is connected to
                          (one of `'A'`, `'B'`, `'C'`, `'D'`, `'E'`, `'F'`).
        '''
        
        self.hub = hub
        self.hub.cmd('from spike import ColorSensor')
        self.port = "ColorSensor('" + port + "')"

        

    def get_color(self):
        '''
        Read color
        
        :return color
        '''
        
        ret = self.hub.cmd(f'{self.port}.get_color()')
        return ret

    
    def get_ambient_light(self):
        '''
        Read ambient light value
        
        :return int 0 to 100% light value
        '''
        ret = self.hub.cmd(f'{self.port}.get_ambient_light()')
        return ret
    
    def get_reflected_light(self):
        '''
        Read reflected light value
        
        :return int 0 to 100% light value
        '''
        ret = self.hub.cmd(f'{self.port}.get_reflected_light()')
        return ret 

    def get_rgb_intensity(self):
        '''
        Read rgb intensity value
        
        :return tuple 0 to 1024 analog rgb value
        '''
        ret = self.hub.cmd(f'{self.port}.get_rgb_intensity()')
        print(" DEVO FARE DEI TEST PER FARLO FUNZIONARE")
        return ret 
    
    def get_red(self):
        '''
        Read red intensity value
        
        :return tuple 0 to 1024 analog red value
        '''
        ret = self.hub.cmd(f'{self.port}.get_red()')
        print(" DEVO FARE DEI TEST PER FARLO FUNZIONARE")
        return ret 
    
    def get_green(self):
        '''
        Read red intensity value
        
        :return tuple 0 to 1024 analog green value
        '''
        ret = self.hub.cmd(f'{self.port}.get_green())')
        print(" DEVO FARE DEI TEST PER FARLO FUNZIONARE")
        return ret 
    
    def get_blue(self):
        '''
        Read red intensity value
        
        :return tuple 0 to 1024 analog blue value
        '''
        ret = self.hub.cmd(f'{self.port}.get_blue()')
        print(" DEVO FARE DEI TEST PER FARLO FUNZIONARE")
        return ret 
    
    def light_up(self,light_1 = 100,light_2 = 100,light_3 = 100):
        lights = []
        lights[0] = light_1
        lights[1] = light_2
        lights[2] = light_3
        i = 0
        while i < 3:
            if lights[i] > 100:
                lights[i] = 100
            elif lights[i] < 0:
                lights[i] = 0
            i += 1

        self.hub.cmd(f'{self.port}.light_up({light_1},{light_2},{light_3})')

    def light_up_all(self,brightness = 100):

        if brightness > 100:
            brightness = 100
        elif brightness < 0:
            brightness = 0
            
        self.hub.cmd(f'{self.port}.light_up_all({brightness})')