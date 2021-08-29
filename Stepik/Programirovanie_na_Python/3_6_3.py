import requests

url_pattern = 'https://stepik.org/media/attachments/course67/3.6.3/'

with open('dataset_3378_3.txt') as in_f_obj:
	url = in_f_obj.read().strip()

counter = 0


while True:
	r = requests.get(url)
	if 'We' in str(r.text.strip()):
		break
	url = url_pattern + str(r.text.strip())
	#print(str(counter) + ' ' + url)
	#counter += 1

text = r.text.strip()

with open('output2.txt', 'w') as out_f_obj:
	out_f_obj.write(text)