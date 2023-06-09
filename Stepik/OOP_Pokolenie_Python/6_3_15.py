def log_for(logfile, date_str):
    with (open(logfile, mode='r', encoding='utf-8') as read_file,
          open(f'log_for_{date_str}.txt', mode='w', encoding='utf-8') as write_file
          ):
        [write_file.write(i[11:]) for i in read_file if date_str in i]
