GS = str(input())
le = len(GS)
cnt = GS.upper().count('G') + GS.upper().count('C')
print((cnt/le)*100)
