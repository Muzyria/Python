# put your python code here
boys = int(input())
blist = list(map(int,input().split()))
girls = int(input())
glist = list(map(int,input().split()))
count = 0 
blist.sort()  
glist.sort()
while blist and glist:
    if blist[0] == glist[0] or blist[0] == glist[0] + 1 or blist[0] == glist[0] - 1:
        count = count + 1
        blist = blist[1:]      # или blist.pop(0)
        glist = glist[1:]      # или glist.pop(0)        
        
    elif blist[0] != glist[0] + 1 or blist[0] != glist[0] - 1:
        blist = blist[1:]
        glist = glist[1:]
print(count)  