with open("logfile.txt", "r", encoding="utf-8") as file_input, open("output.txt", "w", encoding="utf-8") as file_output:
    for line in file_input:
        user, start_time, end_time = line.strip().split(",")

        start_time = start_time.strip().split(":")
        end_time = end_time.strip().split(":")

        start_time = int(start_time[0]) * 60 + int(start_time[1])
        end_time = int(end_time[0]) * 60 + int(end_time[1])

        if end_time - start_time >= 60:
            file_output.write(f"{user}\n")