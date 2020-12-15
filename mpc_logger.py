from datetime import datetime

def log_uid(uid_in):
    log_file = open("output.csv", "a")
    # format: datetime,UID,\n\r
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    log_entry_str = dt_string + ',' + uid_in + '\n'
    log_file.write(log_entry_str)
    log_file.close()