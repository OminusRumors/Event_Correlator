import re

usr=input("Type 1 for test, 2 for events log, 3 for traffic log: ")

if usr == str(1):
	file=open("C:/Users/George/Desktop/Logs/forti_mini.csv", "r")
elif usr == str(2):
	file=open("C:/Users/George/Desktop/Logs/forti_event_9_27.csv", "r")
elif usr == 3:
	file=open("C:/Users/George/Desktop/Logs/forti_traffic_12_15.csv", "r")

attr_list=[]
saver = open("C:/Users/George/Desktop/Logs/list.txt", "w")
saver2 = open("C:/Users/George/Desktop/Logs/list2.txt", "w")
file=file.readlines()[:10000]

for line in file:
	line_list=[]
	del_list=[]
	line_list=re.split('[^\w+=?\w*|\-|\.|\:|\/]', line)
	line_list=list(filter(None, line_list))
	for i in line_list:
		saver.write("{}: {}\n".format(line_list.index(i), i))
	for i in line_list:
		if "=" not in i:
			svd_idx = line_list.index(i)
			line_list[svd_idx - 1] += line_list[svd_idx]
			del line_list[svd_idx]
	for i in line_list:
		attr = i.split('=')[0]
		if attr not in attr_list:
			attr_list.append(attr)

for i in attr_list:
	saver2.write("{}: {}\n".format(attr_list.index(i) + 1, i))
saver.close()
saver2.close()