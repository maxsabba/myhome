from time import sleep
import serial

ser = serial.Serial('/dev/cu.usbmodem1421', 9600)  # only for my mac
counter = 0


while counter < 10:
    # print 'sto inviando: ' + chr(counter)
    ser.write(99)
    print ser.readline()
    sleep(.1)
    counter += 1
