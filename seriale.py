import serial
ser = serial.Serial('/dev/ttyACM2')  # open serial port
stampa = "print(qulo)"
qulo = "qulo = 1"
ser.write(qulo.encode("utf-8"))         # check which port was really used
ser.write(stampa.encode("utf-8"))

while True:
    i = 0
    gay = []
    while i < 100:
        gay.append(ser.read().decode("utf-8"))    # write a string
        i += 1
    print(gay)
ser.close()    