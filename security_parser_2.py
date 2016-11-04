import xml.etree.ElementTree as ET
import sqlite3 as sql
import datetime
from timeit import default_timer
import pdb

tree = ET.parse('C:/Users/George/Desktop/Logs/ad4672.xml')
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
	elif str_value.startswith("{http://schemas.microsoft.com/win/2004/08/events/event}"):
		return str_value[55:]
	else:
		return str_value

#For each event
for child in root:
	values = []
	columns = []
	data_cols = []
	data_cols_str = ""
	data_row = []
	data_row_str = ""

	#Get the "system" part of the log file.
	for c in child[0]:
		if concat(c.tag) == 'EventRecordID':
			dt_recordID = c.text
			values.append(c.text)
			columns.append(concat(c.tag))
		if c.text is None and c.attrib is not None: 
			if c.tag == '{http://schemas.microsoft.com/win/2004/08/events/event}TimeCreated':
				dt = datetime.datetime.strptime(concat(c.attrib), '%Y-%m-%dT%H:%M:%S.%f')
				columns.append(concat(c.tag))
				values.append(dt)
				''''dt_date = dt.date()
				dt_time = dt.time().strftime('%H:%M:%S.%f')
				values.append(dt_date)
				values.append(dt_time)'''
			elif c.tag == '{http://schemas.microsoft.com/win/2004/08/events/event}Execution':
				exe = root.find('./{http://schemas.microsoft.com/win/2004/08/events/event}Event/{http://schemas.microsoft.com/win/2004/08/events/event}System/{http://schemas.microsoft.com/win/2004/08/events/event}Execution')
				columns.append("ProcessID")
				columns.append("ThreadID")
				values.append(exe.attrib['ProcessID'])
				values.append(exe.attrib['ThreadID'])
			else:
				columns.append(concat(str(c.tag)))
				values.append(concat(str(c.attrib)))
		elif c.attrib is None and c.text is not None:
			columns.append(concat(str(c.tag)))
			values.append(concat(str(c.text)))
		elif c.attrib is not None and c.text is not None:
			columns.append(concat(str(c.tag)))
			values.append(concat(str(c.attrib) + concat(c.text)))
		else:
			columns.append(concat(str(c.tag)))
			values.append(concat(c.text))

	#Get the "data" part of the log file.
	for c in child[1]:
		if concat(str(c.attrib)) not in data_cols:
			columns.append(concat(c.attrib))
			values.append(concat(c.text))

		''''#Put the primary keys for the "Security details" table
		data_cols.append('DateCreated')
		data_row.append(dt_date)
		data_cols.append('TimeCreated')
		data_row.append(dt_time)
		data_cols.append('eventRecordID')
		data_row.append(dt_recordID)'''
	print (dt_recordID)
	if len(columns) == len(values):
		data_cols_str = ",".join(str(item) for item in columns)
		data_row_str = ",".join("?" * len(values)) #formats the data_row_str to "?,?,?,?,?,?,?"
		stm='INSERT OR REPLACE INTO security_table (%s) VALUES (%s)' % (data_cols_str, data_row_str)
		#cur.execute('INSERT OR IGNORE INTO Security_log VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', values)
		cur.execute(stm, values)
		conn.commit()
	else:
		print ("Values and columns don't match. " + dt_recordID)
print ("Duration: " + str(default_timer()-start_time))