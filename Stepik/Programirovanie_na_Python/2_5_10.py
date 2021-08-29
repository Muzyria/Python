spisok=[int(i) for i in input().split()]
out=[]
if len(spisok)==1:
  print(spisok[0])
else:
  for i in range(len(spisok)-1):
    print(spisok[i-1]+spisok[i+1], end=' ')
  print(spisok[-2]+spisok[0])