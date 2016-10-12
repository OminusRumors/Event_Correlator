file=open('C:/Users/George/Desktop/Logs/attr2.txt', 'r')

lines = file.readlines()
attr_str=""

for line in lines:
	attr_str += " TEXT, " +line
import sqlite3 as sql
query = 'CREATE TABLE firewall_traffic_log (%s)' % (attr_str)
print (query)
con = sql.connect('C:/Users/George/Desktop/software tools/test.db')
cur = con.cursor()

cur.execute(query)
con.commit()
