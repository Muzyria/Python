a = "123.5.200.1"


print(all(map(lambda x: x.isdigit(), a.split("."))))


