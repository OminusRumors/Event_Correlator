import xml.etree.ElementTree as ET
import sqlite3 as sql
import datetime
from timeit import default_timer
import pdb

tree = ET.parse('C:/Users/George/Desktop/Logs/ad.xml')
root = tree.getroot()
conn = sql.connect('test.db')
cur = conn.cursor()
start_time = default_timer()

def concat(str_value):
	str_value = str(str_value)
	if str_value.startswith('{}'):
		return str_value[2:]
	elif str_value.startswith("{'SystemTime': "):
		print (str_value[16:39])
		return str_value[16:39]
	else:
		return str_value

#{'SystemTime': '2016-09-16T08:34:45.700979700Z'}
for child in root[:10]: #tag="{http://schemas.microsoft.com/win/2004/08/events/event}Provider"
	values = []
	data_str = ''
	#Get the "data" part of the log file.
	for c in child[1]:
		data_str += concat(str(c.attrib)) + concat(str(c.text))
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
			values.append(concat(c.text))
		elif c.attrib is not None and c.text is not None:
			values.append(concat(str(c.attrib) + concat(c.text)))
		else:
			values.append(concat(c.text))
	for v in values:
		print(v)
	values.append(concat(data_str))
	cur.execute('INSERT INTO [Security-parsed-log] VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', values)
	conn.commit()
		#print (child[1][0].tag, child[1][0].attrib, child[1][0].text)
		#cur.execute('INSERT INTO Security-parsed-log VALUES ')
print ("Duration: " + str(default_timer()-start_time))