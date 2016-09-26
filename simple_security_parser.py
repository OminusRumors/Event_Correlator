import xml.etree.ElementTree as ET
import sqlite3 as sql
import datetime
from timeit import default_timer
import pdb

tree = ET.parse('C:/Users/George/Desktop/Logs/ad.xml')
root = tree.getroot()
conn = sql.connect('C:/Users/George/Desktop/software tools/test.db')
cur = conn.cursor()
start_time = default_timer()

def concat(str_value):
	str_value = str(str_value)
	if str_value.startswith('{}'):
		return str_value[2:]
	elif str_value.startswith("{'SystemTime': "):
		return str_value[16:42]
	elif str_value.startswith("{'Name': "):
		return str_value[10:-2].lower()
	else:
		return str_value

for child in root[:10]:
	values = []
	data_cols = []
	data_cols_str = ""
	data_row = []
	data_row_str = ""
	#Get the "system" part of the log file.
	for c in child[0]:
		if c.text is None and c.attrib is not None: 
			if c.tag == '{http://schemas.microsoft.com/win/2004/08/events/event}TimeCreated':
				#pdb.set_trace()
				dt = datetime.datetime.strptime(concat(c.attrib), '%Y-%m-%dT%H:%M:%S.%f')
				dt_date = dt.date()
				dt_time = dt.time().strftime('%H:%M:%S.%f')
				values.append(dt_date)
				values.append(dt_time)	
			else:
				values.append(concat(str(c.attrib)))
		elif c.attrib is None and c.text is not None:
			if c.tag == '{http://schemas.microsoft.com/win/2004/08/events/event}EventRecordID':
				dt_recordID = c.text
			values.append(concat(c.text))
		elif c.attrib is not None and c.text is not None:
			values.append(concat(str(c.attrib) + concat(c.text)))
		else:
			values.append(concat(c.text))
	#Get the "data" part of the log file.
	for c in child[1]:
		if concat(str(c.attrib)) not in data_cols:
			data_cols.append(concat(c.attrib))
			data_row.append(concat(c.text))
	data_cols_str = ",".join(str(item) for item in data_cols)
	data_row_str = ",".join("?" * len(data_row))
	stm='INSERT INTO security_details (%s) VALUES (%s)' % (data_cols_str, data_row_str)
	file = open("C:/Users/George/Desktop/software tools/detail_attrib.txt","w")
	file.write(stm)
	file.close()
	cur.execute('INSERT INTO [Security-parsed-log] VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', values)
	cur.execute(stm, data_row)
	conn.commit()
		#print (child[1][0].tag, child[1][0].attrib, child[1][0].text)
		#cur.execute('INSERT INTO Security-parsed-log VALUES ')
print ("Duration: " + str(default_timer()-start_time))