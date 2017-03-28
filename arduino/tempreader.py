from __future__ import print_function
import serial
import sqlite3 as lite
import time
import sys
from datetime import datetime


con = None
count = 0

def readfromserial():
    # set serial inteface to read data from arduinoSerialData
    arduinoSerialData = serial.Serial('/dev/ttyACM0', 9600)
    myData = arduinoSerialData.readline()
    # myData = "Stanza1; 30.9"
    # print('Ciclo while')
    return myData


try:
    while count < 100:
        con = lite.connect('../database/myhome.db')
        cur = con.cursor()
        # add the selcet query
        # today = str(datetime.now())
        fromSer = readfromserial()
        print(fromSer)
        cur.execute("INSERT INTO temperature (readingtime,arduino_id,tempvalue) \
        VALUES (?, ?, ?);", (str(datetime.now()), fromSer.split(';')[0], fromSer.split(';')[1]))
        data = cur.fetchone()
        print("SQLite messagge: %s" % data)
        con.commit()
        time.sleep(10)
        count = count + 1



except lite.Error, e:
    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()
