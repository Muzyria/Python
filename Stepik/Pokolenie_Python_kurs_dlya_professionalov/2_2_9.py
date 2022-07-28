

path = rf'files.txt'
with open(path, "r", encoding="UTF-8") as file:
    for line in file.readlines():
        name, size, units = line.rstrip().split()
        ext = name.split(".")[1]
        print(name, ext, size, units, "++++++")


# size_res.setdefault(name.split('.')[1], {}).setdefault(units, []).append(int(size))
