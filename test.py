# from datetime import datetime
# today = datetime.today()
# print(today)
# date_time = today.strftime("%A %H %M").split()
# print(date_time)
# curr_day, curr_hour, curr_min, curr_sec = date_time
# print(curr_day, curr_hour, curr_min, curr_sec)
# class1 = (9, 40)
# test = (1, 2, *class1)
# print(test)
from timetable import time_table
from datetime import datetime
now = datetime.today()
curr_day, curr_hour, curr_min = now.strftime("%A %H %M").split()
tt = enumerate(time_table[curr_day])
weekly_tt = []
    # curr_class, class_hour, class_min = (j[i] for i,j in tt)
# curr_class, class_hour, class_min = [i[0] for i in tt]