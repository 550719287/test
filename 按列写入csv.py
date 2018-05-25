#coding:utf-8
# a = [1,2,3,4,5,6,7]
# b = []
# for i in a:
# 	print i
# 	b.append(i)
# if a == b :
# 	print ('ok')
# 	print(a[0])
# 	print(a[-1])

import csv

with open('D:/1.csv', mode='wb') as fp1, open('D:/2.csv', 'rb') as fp2, open('D:/3.csv', 'rb') as fp3:
	fieldnames1 = ['first']
	fieldnames2 = [1,'2','3','4','5','6']
	write1 = csv.DictWriter(fp1, fieldnames1)

	write1.writeheader()
	for i in fieldnames2:
		file3 = {}
		file3 = dict(zip(fieldnames1, [i]))
		print file3
		write1.writerow(file3)