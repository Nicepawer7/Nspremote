class Button:
    '''
    A button (left, right) of a hub block including button
    lights.
    '''
        
    def __init__(self, hub, which):
        '''
        Prepare hub for button usage.
    
        :param Hub hub: [](#Hub) object the button belongs to.
        'param str which: Button identifier (`'left'`,
                          `'right`')
        '''
        
        self.hub = hub
        self.which = which
    
    def set_color(self, color):
        '''
        Set the button light's color.
        
        :param int color:  Values 1 to 11 select one of
                          the hub's predefined colors.
        '''
        
        self.hub.cmd(f"spike.status_light.on('{color}')")

    def turn_light_off(self):
        '''
        Set the button light off.
        '''
        
        self.hub.cmd(f"spike.status_light.off()")        
        
    def is_pressed(self):
        '''
        Returns number of milliseconds the button is down for.
        
        :return int: Button down time in milliseconds. If button isn't down, 0
                     is returned.
        '''
        
        ret = self.hub.cmd(f'spike.{self.which}.is_pressed()')
        
        return int(ret)
