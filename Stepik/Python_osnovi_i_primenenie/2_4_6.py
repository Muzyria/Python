import os

with open("2_4_6.txt", "w") as file:
    for curr_dir, dirs, files in os.walk("main"):
        # print(curr_dir, dirs, files)
        if set(filter(lambda x: x.endswith(".py"), files)):
            # print(curr_dir)
            file.write(curr_dir + "\n")



