import sqlite3 as sql
import xml.etree.ElementTree as ET

def concat(value):
	return value[10:-2].lower()

conn=sql.connect('C:/Users/George/Desktop/software tools/test.db')
cur=conn.cursor()

tree = ET.parse('C:/Users/George/Desktop/Logs/ad.xml')
root = tree.getroot()

detail_list=[]

#Get cols names
for child in root:
	for c in child[1]:
		if concat(str(c.attrib)) not in detail_list:
			detail_list.append(concat(str(c.attrib)))

str_cols=""
for v in detail_list:
	str_cols += "{0} TEXT\n, ".format(v)

stm="CREATE TABLE security_details ({0} DateCreated DATE, TimeCreated TIME, eventRecordID INT, FOREIGN KEY (DateCreated, TimeCreated, EventRecordID) REFERENCES [Security-parsed-log](DateCreated, TimeCreated, EventRecordID))".format(str_cols)
print (stm)
cur.execute(stm)
conn.commit()