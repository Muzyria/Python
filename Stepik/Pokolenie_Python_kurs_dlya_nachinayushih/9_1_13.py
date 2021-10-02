# put your python code here
stok = input()
count = 0
for i in range(1, len(stok)):
    if stok[i -1] == stok[i]:
        count += 1  
print(count) 