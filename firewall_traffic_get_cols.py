import csv

attr_list=[]
inst_list=[]
attr_str
saver = open('C:/Users/George/Desktop/Logs/attr2.txt', 'w')
with open('C:/Users/George/Desktop/Logs/forti_traffic_12_15.csv', newline='') as file:
	reader=csv.reader(file)
	for i in reader[:10000]:
		row = next(reader)
		for item in row:
			if item == '':
				del item
			else:
				try:
					attr = item.split('=')[0]
					inst = item.split('=')[1]
					if attr not in attr_list:
						attr_list.append(attr)
						saver.write(attr + "\n")
				except:
					print ("You fucked up: {}".format(item))
