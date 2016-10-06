import re
import pdb
import sqlite3 as sql

usr=input("Type 1 for test, 2 for events log, 3 for traffic log: ")

if usr == str(1):
	file=open("C:/Users/George/Desktop/Logs/forti_mini.csv", "r")
elif usr == str(2):
	file=open("C:/Users/George/Desktop/Logs/forti_event_9_27.csv", "r")
elif usr == 3:
	file=open("C:/Users/George/Desktop/Logs/forti_traffic_12_15.csv", "r")

attr_list=[]
attr_str=""
counter = 0
saver = open("C:/Users/George/Desktop/Logs/list_bef.txt", "w")
saver2 = open("C:/Users/George/Desktop/Logs/attr.txt", "w")
saver3 = open("C:/Users/George/Desktop/Logs/list_aft.txt", "w")
file=file.readlines()[:40000]

for line in file:
	line_list=[]
	line_list=re.split('[^\w+=?\w*|\-|\.|\:|\/|\s]', line)
	line_list=list(filter(None, line_list))
	saver.write(str(counter) + "-" * 30)
	#for i in line_list:
	#	saver.write("{}: {}\n".format(line_list.index(i), i))
	'''
	This "for" correlates the values with their key. Eg:
	LIST BEFORE:	LIST AFTER:
	...=...			...=...
	...=...			...=...
	...=			...=...
	...				...
	...=...			...=...
	...=			...=...
	...				...
	'''
	for i in range(0, len(line_list)):
		if line_list[i].endswith("="):
			line_list[i] += line_list[i+1]
	'''
	This "for" deletes the extra values that don't have a key, and gets all the attributes.
	'''
	for i in line_list:
		if '=' not in i:
			line_list.pop(line_list.index(i))
			continue
		attr = ""
		attr = i.split('=')[0]
		if attr not in attr_list and not attr.startswith(' '):
			attr_list.append(attr)
			saver2.write(attr + "\n")
	saver3.write(str(counter) + "-" * 30)
	counter += 1

for i in attr_list[:-1]:
	attr_str += '{} VARCHAR,'.format(i)
attr_str += '{} VARCHAR'.format(line_list[-1])

query = "CREATE TABLE firewall_log ({})".format(attr_str)
saver.write(query)
conn=sql.connect('C:/Users/George/Desktop/software tools/test.db')
cur=conn.cursor()
cur.execute(query)
conn.commit()
conn.close()
saver.close()
saver2.close()
saver3.close()