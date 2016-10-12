import xml.etree.ElementTree as ET
import datetime
import collections
from timeit import default_timer

def concat(value):
	return value[10:-2].lower()

tree = ET.parse('C:/Users/George/Desktop/Logs/ad.xml')
root = tree.getroot()

detail_list=[]
cnt = 0

for child in root:
	for c in child[0]:
		if c.tag == '{http://schemas.microsoft.com/win/2004/08/events/event}TimeCreated':
			dt = datetime.datetime.strptime(concat(c.attrib), '%Y-%m-%dT%H:%M:%S.%f')
			dt_date = dt.date()
			dt_time = dt.time().strftime('%H:%M:%S.%f')
		if c.tag == '{http://schemas.microsoft.com/win/2004/08/events/event}EventRecordID':
			recordID = c.text

	for c in child[1]:
		if concat(str(c.attrib)) not in detail_list:
			detail_list.append(concat(str(c.attrib)))
			file.write(concat(str(c.attrib)))
			cnt+=1
file.close()

for value in sorted(detail_list):
	print (value)
print(cnt)
