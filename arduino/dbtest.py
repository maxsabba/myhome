import sqlite3 as lite
import sys


con = None


try:
    # work on mac with virtual env
    con = lite.connect('../database/myhome.db')
    # work on production
    # con = lite.connect('~/myhome/database/myhome.db')

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print "SQLite version: %s" % data

except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)


finally:
    if con:
        con.close()
