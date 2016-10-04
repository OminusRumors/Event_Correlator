#12.23.35
import xml.etree.ElementTree as ET

tree = ET.parse('C:/Users/George/Desktop/Logs/ad.xml')
root = tree.getroot()

#For each event
for child in root[:1]:
	for c in child[0]:
		print (c.tag)
		print (c.attrib)
		print (c.text)
		print ('-' * 50)