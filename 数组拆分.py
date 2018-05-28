#coding=utf-8

with open('/home/user/workspace/zh_nan/task/categoryid_1.csv', 'r') as csvlist1, open(
		'/home/user/workspace/zh_nan/task/categoryid_2.csv', 'r') as csvlist2:
	list1 = []
	list2 = []
	readlist1 = csv.DictReader(csvlist1)
	readlist2 = csv.DictReader(csvlist2)

	for first in readlist1:
		# 从文件读取id
		list1.append(first['CategoryId'])
	for second in readlist2:
		# print '12',second['CategoryId']
		list2.append(second['CategoryId'])
	# print len(self.count_list)
	for j in self.count_list:
		# count_list存的是每个一级单元包含多少二级单元
		if j == 0:
			# 一级单元包含0个二级
			self.count_secondlist.append([])
		else:
			# 将数据按照二级list为单位拆分重组成新数组
			lis = []
			for n in range(j):
				lis.append(list2[0])
				del list2[0]
			# print lis
			self.count_secondlist.append(lis)
			# print self.count_secondlist
			
