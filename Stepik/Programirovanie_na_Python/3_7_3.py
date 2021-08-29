d = int(input())
#words = []
words = set()
#unknow_words = []
unknow_words = set()	

for _ in range(d):
	#words.append(input().lower())
	words.add(input().lower())

l = int(input())


for _ in range(l):
	string = input().lower().split()
	
	for i in range(len(string)):
		if string[i] not in words:
			#unknow_words.append(string[i])
			unknow_words.add(string[i])
			
for word in unknow_words:
	print(word)