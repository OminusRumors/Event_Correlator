file=open("C:/Users/George/Desktop/Logs/forti_mini.csv", "r")
attr_list=[]
for line in file:
	#print (line)
	line_list=[]
	line_list=line.split(",")
	for inst in line_list:
		attr=inst.split("=")[0]
		attr=attr[1:]
		#print (attr)
		if attr not in attr_list and attr != '"' and attr != '""' and attr != '"""':
			attr_list.append(attr) #returns 2 value list [attribute, instance]
for item in attr_list:
	print(item)
