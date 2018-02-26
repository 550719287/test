#coding:utf-8
import win32gui
import win32api
import win32con
import win32process

import sys
# 获取窗体句柄
# hWnd = win32gui.GetForegroundWindow()
# #获取光标句柄
# FormThreadID = win32api.GetCurrentThreadId()
# print(FormThreadID)
# #获取窗体对应线程id、进程id
# CWndThreadID = win32process.GetWindowThreadProcessId(hWnd)
# print(CWndThreadID[1])

# AttachThreadInput(CWndThreadID[0], FormThreadID, True) 
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)


# win32gui.PostMessage(hWnd,win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

# win32gui.PostMessage(hWnd,win32con.WM_KEYUP, win32con.VK_RETURN, 0)
# def returnuse(max):

# 	mem = []

# 	for a in range(0,max):
# 		while a in mem:
# 			break
# 		else:
# 			print a
# 			use = a
# 			mem.append(a)
# 			print mem
# 			break
# 	return use

# print returnuse(5)
# 
import numpy as np

# X = [[1,2,3],
# 	 [2,3,4],[1,2,3]]
# X = np.atleast_2d(X)
# print X
# temp = np.ones([X.shape[0], X.shape[1]+1]) #初始化矩阵
# print temp
# x = np.atleast_2d(X)
# temp[:,0:-1] = x
# print temp[:,0:-1]
sizes = [3,4,2]
w_ = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
print np.random.randn(4, 1)


