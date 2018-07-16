#coding=utf-8



# wb = load_workbook(filename)
# sheet = wb1["Sheet1"]
# maxrow = sheet.max_row
# maxcol = sheet.max_column
# 从excel导入


# lis2 = []
# lis2.extend([lis1[0]])
# del lis1[0]
# print lis1 , lis2
# 


# 		# break#跳出循环
# 		pass#继续执行下一个直到结束
# 		# return#终止函数
# 	else:
# 		print '11'
# 	print 23

# func([2,3,3],[2,2,2])
# print lis1

# for j in lis1:
# 	print j
# 	dic2["%s"%j] = ""
# print dic2.get('1')
# # dic2.get('1')=('11')
# dic2['1'] = 'ww'
# print dic2['1']
# # print lis1

# dic1 = {'1':{'11':{'111':{'1111':{'11111':{'111111':'123'}}}}},'13':''}
# print dic1.values()
# for i in dic1.values():
# 	print type(i)
# 	if type(i) is dict:
# 		print i.values()

# excelfilename = 'C:\Users\Administrator.NEU-20180426WRL\Desktop\POI_report'
# wb = load_workbook(excelfilename)
# wr = Workbook()
# list1 = ['1','2','3','4','5']
# w1 = wr.creat_sheet('Test1')
# w1.append(list1)
# dic2 = {'1':'11','2':'22','3':{'33':333},'4':{'44':{'444':{'4444':'end'}}}}
# print type(dic2['3']['33'])
# for first in dict2.keys():
	
# 	write first
# 	if type(dic2[first]) is not dict:
# 		write dic2[first]
# 	else:
# 		for second in dic2[first].keys():
# 			if dic2[first].values() == '':
# 				write second
# 			else:
# 				write second
# 				for third in  dic2[first][second].keys():
# 					if dic2[first][second].values() == '':

def demo():
	a = 4
	b = 5
	return a,b

def func(a,b):
	for n in b:
		for i in a:
			if i>3:
				pass
			elif i>1:
				pass
				if i>0:
					pass
				elif i<4:
					pass
	return i,n
# n = demo()
# print n

print list(func([3], [4]))
