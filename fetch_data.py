import xml.etree.ElementTree as ET
import datetime
import collections
from timeit import default_timer

def concat(value):
	return value[10:-2].lower()

tree = ET.parse('C:/Users/George/Desktop/Logs/ad.xml')
root = tree.getroot()
file = open("detail_attrib.txt", "w")

detail_values={}
detail_list=[]
cnt = 0

for child in root:
	for c in child[1]:
		if concat(str(c.attrib)) not in detail_list:
			detail_list.append(concat(str(c.attrib)))
			file.write(concat(str(c.attrib)))
			cnt+=1
file.close()

for value in sorted(detail_list):
	print (value)
print(cnt)
'''
for child in root: #tag="{http://schemas.microsoft.com/win/2004/08/events/event}Provider"
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
	values.append(concat(data_str))
	cur.execute('INSERT INTO [Security-parsed-log] VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', values)
	conn.commit()
		#print (child[1][0].tag, child[1][0].attrib, child[1][0].text)
		#cur.execute('INSERT INTO Security-parsed-log VALUES ')
print ("Duration: " + str(default_timer()-start_time))'''