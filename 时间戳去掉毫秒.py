import time,datetime

timestamp = time.time()
time1 = time.localtime(timestamp)
time2 = time.strftime("%Y-%m-%d %H:%M:%S",time1)
print timestamp ,time1
print time2
d1 = datetime.datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime('2012-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
delta = d1 - d2
print delta
