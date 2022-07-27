
lst = [input() for _ in range(3)]

ru, en = 0, 0

for char in lst:
    if char in "AaBCcEeHKMOoPpTXxy":
        en += 1
    if char in "АаВСсЕеНКМОоРрТХху":
        ru += 1

if ru == 3:
    print("ru")
elif en == 3:
    print("en")
else:
    print("mix")


