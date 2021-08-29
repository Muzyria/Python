class_rawinfo = {}
#new_heights = 0
#new_students = 0
class_info = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
#class_info = []

with open('dataset_3380_5.txt') as in_f_obj:
	for line in in_f_obj:
		#print(line)
		string = line.rstrip().split('\t')
		#print(string)
#n = int(input())
#for _ in range(n):
	#string = input().split('	')
		if string[0] not in class_rawinfo:
			class_rawinfo[string[0]] = [int(string[2]), 1]
		elif string[0] in class_rawinfo:
			heights = class_rawinfo[string[0]][0] + int(string[2])
			students = class_rawinfo[string[0]][1] + 1
			class_rawinfo[string[0]] = [heights, students]

for k, v in class_rawinfo.items():
	#print(k, str(v[0] / v[1]))
	#list.pop([int(k)-1])
	class_info[int(k)-1] = v[0] / v[1]
	#print(class_rawinfo)
	#print(class_info)

with open('output.txt', 'w') as out_f_obj:	
	for i in range(len(class_info)):
		#print(i+1, str(class_info[i]))
		output = str(i+1) + ' ' + str(class_info[i]) + '\n'
		#print(output)
		out_f_obj.write(output)