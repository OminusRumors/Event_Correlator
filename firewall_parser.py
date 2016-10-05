import re
import pdb

usr=input("Type 1 for test, 2 for log file: ")

if usr == str(1):
	file=open("C:/Users/George/Desktop/Logs/forti_mini.csv", "r")
elif usr == str(2):
	file=open("C:/Users/George/Desktop/Logs/forti_event_9_27.csv", "r")
else:
	usr=raw_input("Type 1 for test, 2 for log file: ")

attr_list=[]

for line in file:
	line_list=[]
	line_list=re.split('[^\w+=?\w*|\-|\.|\:|\/]', line)
	line_list=list(filter(None, line_list))
	for i in line_list:
		if i.endswith('=') and line_list.index(i) <= len(line_list)-2:
			line_list[line_list.index(i)] += line_list[line_list.index(i)+1]
			try:
				del line_list[line_list.index(i)+1]
			except ValueError:
				pass
	print (line_list)
'''
	for i in range(len(line_list)-1):
		pdb.set_trace()
		if line_list[i].endswith('=') and i <= len(line_list)-2:
			line_list[i] += line_list[i+1]
			del line_list[i+1]
			#line_list.insert(i, line_list[i]+line_list.pop(i+1))
			print (line_list[i])
			if attr not in attr_list:
				attr_list.append(attr) #returns 2 value list [attribute, instance]
'''
for item in attr_list:
	print(item)
