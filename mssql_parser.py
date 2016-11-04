import xml.etree.ElementTree as et
import sqlite3 as sql
import datetime
from timeit import default_timer

def concat(str_value):
	str_value = str(str_value)
	if str_value.startswith('{}'):
		return str_value[2:]
	elif str_value.startswith("{'SystemTime': "):
		return str_value[16:42]
	elif str_value.startswith("{'Name': "):
		return str_value[10:-2].lower()
	elif str_value.startswith("{http://schemas.microsoft.com/win/2004/08/events/event}"):
		return str_value[55:]
	else:
		return str_value

tree = et.parse('C:/Users/George/Desktop/Logs/sql4672.xml')
root = tree.getroot()
conn = sql.connect('C:/Users/George/Desktop/software tools/test.db')
cur = conn.cursor()

start = default_timer()

for event in root:
	cols=[]
	cols_str=""
	values=[]
	for sys in event[0]:
		if sys.attrib is None and sys.text is not None:
			cols.append(concat(sys.tag))
			values.append(concat(sys.text))
		elif sys.attrib is not None and sys.text is None:
			if concat(sys.tag) == 'Execution':
				cols.append('ProcessID')
				values.append(sys.attrib['ProcessID'])
				cols.append('ThreadID')
				values.append(sys.attrib['ThreadID'])
			elif concat(sys.tag) == 'TimeCreated':
				cols.append('TimeCreated')
				values.append(str(sys.attrib['SystemTime']))
			else:
				cols.append(concat(sys.tag))
				values.append("Microsoft-Windows-Security-Auditing")
		else:
			cols.append(concat(sys.tag))
			values.append(concat(sys.attrib) + concat(sys.text))
	for det in event[1]:
		cols.append(concat(det.attrib).lower())
		values.append(concat(det.text))
	print (values[8])
	cols_str = ",".join(str(i) for i in cols)
	row_str = ",".join("?" * len(values))
	query = 'INSERT OR REPLACE INTO mssql_table (%s) VALUES (%s);' % (cols_str, row_str)
	cur.execute(query, values)
	conn.commit()

conn.close()
print ('Duration in sec: ' + str(default_timer()-start))