import sqlite3 as sql
import xml.etree.ElementTree as ET

def concat(value):
	if value.startswith('{http://schemas.microsoft.com/win/2004/08/events/event'):
		return value[55:]
	else:
		return value[10:-2].lower()


tree = ET.parse('C:/Users/George/Desktop/Logs/mssql.xml')
root = tree.getroot()

detail_list=[]
file=open('system.txt', 'w')

#Get cols names
for child in root:
	for c in child[0]:
		if concat(str(c.tag)) not in detail_list:
			detail_list.append(concat(str(c.tag)))
	for c in child[1]:
		if concat(str(c.attrib)) not in detail_list:
			detail_list.append(concat(str(c.attrib)))
#End of getting col names

str_list=""
for t in detail_list[:-1]:
	str_list += '{} TEXT,\n'.format(t)
str_list += '{0} {1}'.format(detail_list[-1], 'TEXT')
file.write(str_list)

conn=sql.connect('C:/Users/George/Desktop/software tools/test.db')
cur=conn.cursor()

query='CREATE TABLE mssql_table ({})'.format(str_list)
file.write("\n"+query)
cur.execute(query)
conn.commit()