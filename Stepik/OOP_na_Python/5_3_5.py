try:
    file = open('pentagon_secrets.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print("Эх, не судьба тайны пентагона узнать")    