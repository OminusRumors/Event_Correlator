import sqlite3 as sql
import re

file = open("C:/Users/George/Desktop/Logs/forti_event_9_27.csv", "r")

con = sql.connect('C:/Users/George/Desktop/software tools/test.db')
cur = con.cursor()

for line in file:
	attr_str=""
	inst_list=[]
	line_list=[]
	line_list=re.split('[^\w+=?\w*|\-|\.|\:|\/|\s]', line)
	line_list=list(filter(None, line_list))

	#Assign alone keys with their values
	for i in range(0, len(line_list)):
		if line_list[i].endswith("="):
			line_list[i] += line_list[i+1]

	#Delete lone values after assignment and populate attr and inst lists
	for i in line_list:
		if '=' not in i:
			line_list.pop(line_list.index(i))
			continue
		else:
			attr_str += "{} ,".format(i.split('=')[0])
			inst_list.append(i.split('=')[1])
	attr_str = attr_str[:-1]
	query = "INSERT OR REPLACE INTO firewall_event_log (%s) VALUES (%s)" % (attr_str, ", ".join("?" * len(inst_list)))
	try:
		cur.execute(query, inst_list)
		con.commit()
	except:
		con.rollback()
		continue
con.close()
