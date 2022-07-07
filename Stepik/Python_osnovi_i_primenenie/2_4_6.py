import os

with open("2_4_6.txt", "w") as file:
    for curr_dir, dirs, files in os.walk("main"):
        # print(curr_dir, dirs, files)

        print(files)


