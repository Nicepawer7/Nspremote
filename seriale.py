import spremote
from time import sleep



print('Press left button to reduce speed, right button to increase speed, ' + \
      'both buttons to stop the program.')

hub = spremote.Hub('/dev/ttyACM1')
lb = spremote.Button(hub, 'LEFT')
rb = spremote.Button(hub, 'RIGHT')
m = spremote.MotorPair(hub, 'A','B')



m.start(30)
sleep(10)
m.stop()

hub.disconnect()
