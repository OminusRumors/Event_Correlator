import csv
import sqlite3 as sql

saver = open('C:/Users/George/Desktop/Logs/attr2.txt', 'w')
with open('C:/Users/George/Desktop/Logs/forti_traffic_12_15.csv', newline='') as file:
	con = sql.connect('C:/Users/George/Desktop/software tools/test.db')
	cur = con.cursor()
	reader=csv.reader(file)
	for i in range(10000):
		row = next(reader)
		attr_str = ""
		inst_list=[]
		for item in row:
			if item == '':
				del item
			else:
				try:
					attr = item.split('=')[0]
					inst_list.append(item.split('=')[1])
					attr_str += attr + ", "
				except:
					print ("You fucked up: {}".format(item))
		attr_str = attr_str[:-2]
		query = "INSERT OR REPLACE INTO firewall_traffic_log (%s) VALUES (%s)" % (attr_str, ", ".join("?" * len(inst_list)))
		cur.execute(query, inst_list)
		con.commit()
