# import Serial
import sqlite3
import sys
from datetime import datetime

# set serial inteface to read data from arduinoSerialData
arduinoSerialData = serial.Serial('/dev/ttyACM0', 9600)

while 1:
    myData = arduinoSerialData.readline()


con = None

try:
    con = sqlite3.connect('../database/myhome.db')
    cur = con.cursor()
    # add the selcet query
    # today = str(datetime.now())
    # print today
    cur.execute("INSERT INTO temperature (readingtime,arduino_id,tempvalue) \
    VALUES (?, ?, ?);",(str(datetime.now()), myData.split(';')[0], myData.split(';')[1]))
    data = cur.fetchone()
    print "SQLite messagge: %s" % data
    con.commit()


except sqlite3.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:
    if con:
        con.close()
