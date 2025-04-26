import serial

class Hub:
    ''' Connection related functionality of a hub block (no sensors, buttons,
        light matrix aso.). '''
    
    def __init__(self, port):
        '''
        Connect host to the hub's Python interpreter.
    
        :param str port: Device name of the hub at the host machine (e.g.
                         `/dev/ttyACM0`).
        '''
        print("uuuh")
        # connect
        self.connection = serial.Serial(port, 115200, timeout=0.1)
        if not self.connection.is_open:
            print("bleh")
            self.connection.open()

        print("yuuuuuu")
        # stop runloop by Ctrl+D (yields full control over Python interpreter)
        self.connection.write(b'\x03')
        print("Hub initialized")
        # check Python interpreter's greeting message
        self.connection.readlines()
        # prepare for device listing
        self.cmd('import device')
        self.cmd('from spike import PrimeHub')
        self.cmd('spike = PrimeHub()')
        

    def disconnect(self):
        '''
        Close serial connection to hub.
        '''
        
        self.connection.close()
        

    def write(self, text):
        '''
        Send one or multiple lines of text to the hub's Python interpreter
        (almost) as is.
        
        :param str text: String to send to the hub.
        
        If text does not end with `'\\n'`, then `'\\n'` will be appended before
        sending. In addition, the hub's interactive Python interpreter uses
        `'\\r\\n'` for line breaks. Thus, `'\\n'` is replaced by `'\\r\\n'`
        before sending.
        
        ```{note}
        Due to the interpreter's autoindentation feature this method is not
        suitable for sending code blocks with identation. Instead, use [](#cmd)
        to send code blocks.
        ```
        '''
        
        if not text.endswith('\n'):
            text += '\n'
        self.connection.write(text.replace('\n', '\r\n').encode())
        
        
    def readline(self):
        '''
        Read one line from the hub's Python interpreter.
        
        :return str: Text read from hub without trailing line break.
        '''
        
        raw = self.connection.readline()
        if raw[-2:] == b'\r\n':
            text = raw[:-2].decode()
        else:
            text = raw.decode()
        
        return text

    
    def readlines(self):
        '''
        Read all available lines from hub.
        
        Hub line breaks (`'\\r\\n'`) are replaced by `'\\n'`.

        :return str: Text read from hub.
        '''
        
        raw = self.connection.readlines()
        text = ''
        for raw_line in raw:
            if raw_line[-2:] == b'\r\n':
                text += raw_line[:-2].decode() + '\n'
            else:
                text += raw_line.decode()
        
        return text


    def cmd(self, code):
        '''
        Send Python code to the hub.
        
        Waits until interpreter asks for next command and returns output
        shown by the interpreter.
        
        :param str code: Python code to execute on the hub.
        :return [str]: All outputs produced by the code (list of lines).
        '''
        
        marker = '<<<done>>>'
        
        # insert line breaks to cope with the interpreter's autoindentation
        lines = code.split('\n')
        for i in range(len(lines) - 1):
            if lines[i + 1].startswith(' ') or lines[i].startswith(' '):
                lines[i] += '\n\n'
        if lines[-1].startswith(' '):
            lines[-1] += '\n\n'
        lines[-1] += '\n'
            
        # send code
        self.write('\n'.join(lines))
        self.write('#' + marker)
        output = 0
        # wait till executed and collect outputs
        while True:
            line = self.readline()
            if line == '':
                continue
            if line.find(marker) > -1:
                break
            if line[:3] != '>>>' and line[:3] != '...':
                output = line
        return output


    def list_devices(self):
        '''
        List IDs of devices connected to the hub.
        
        Each device type has a unique ID. With this method the port a device is
        connected to can be identified at runtime.
        
        :return dict(str=int): Dictionary with keys `'A'`, `'B'`, `'C'`, `'D'`,
                            `'E'`, `'F'` and integer values representing device
                            IDs. 0 indicates that no device is connect to the
                            port.
        '''
        
        devices = {}
        ports = ['A','B','C','D','E','F']
        for port in ports:
            devices[port] = (self.cmd(f"print(hub.port.{port}.info()['type'])"))
            if devices[port] == "None":
                devices[port] = 0
            else:
                devices[port] = int(devices[port])
        return devices