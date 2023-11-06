#By Daniel(滑稽到滑稽的滑稽)
#安装模块
import time
import random
import requests
import re
import os
import traceback
from tqdm import tqdm
from pygame import mixer
from func_timeout import func_timeout
import socket
import threading
import win32api,win32con
#更改窗口名称
os.system("title Super Dos")
#模拟加载
print("\r328KB OK",end='')
time.sleep(3)
print("\r625KB OK",end='')
time.sleep(1)
print("\r1024KB OK",end='')
time.sleep(0.5)
print("\rcpu:antel s9 10002K",end='')
time.sleep(0.5)
print("\rgpu:stx 4090ti       ",end='')
time.sleep(0.5)
print("\rram:1024KB         ",end='')
time.sleep(1)
os.system("cls")
time.sleep(1)
#设置操作注册表的各种东西
reg_root = win32con.HKEY_CURRENT_USER
reg_path = "SOFTWARE\\Superdos"
reg_flags = win32con.WRITE_OWNER|win32con.KEY_WOW64_64KEY|win32con.KEY_ALL_ACCESS
win32api.RegCreateKeyEx(reg_root, reg_path, reg_flags)
reg_key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
#读取序列号
try:
	key = win32api.RegQueryValueEx(reg_key,"system_key")[0]
except:#判断序列号是否存在，不存在创建
	win32api.RegSetValueEx(reg_key, "system_key", 0, win32con.REG_SZ, str(random.randint(10000000000000, 99999999999999)))
	key = win32api.RegQueryValueEx(reg_key, "system_key")[0]
#读取安全模式是否可以进入
try:
	opensafe = win32api.RegQueryValueEx(reg_key,"safemode_status")[0]
except:
	win32api.RegSetValueEx(reg_key, "safemode_status", 0, win32con.REG_SZ, 'true')
	opensafe = win32api.RegQueryValueEx(reg_key, "safemode_status")[0]
#读取解锁状态
try:
	unlock = win32api.RegQueryValueEx(reg_key,"unlock_status")[0]
except:
	win32api.RegSetValueEx(reg_key, "unlock_status", 0, win32con.REG_SZ, 'false')
	unlock = win32api.RegQueryValueEx(reg_key, "unlock_status")[0]
if os.path.exists('c:\\Windows\\boot.ini'):
	f = open('c:\\Windows\\boot.ini')
	if f.read() == '[info]start system':
		while 1:
			os.system("cls")
			print("The boot file is error")
	f.close()
pygame_init = 0
for i in tqdm(range(100),desc='Loding',unit='kb'):
	time.sleep(0.1)
os.system("cls")
time.sleep(0.5)
def oobe():
	os.system('color f0')
	print('''
                    *********  *******  ******   *******
                    *       *  *     *  *     *  *
                    *       *  *     *  ******   *******
                    *       *  *******  *     *  *
                    *********           ******   *******   
                    ------------------------------------
                    #         欢迎来到SuperDos!         #
                    ------------------------------------''')
	time.sleep(3)
	os.system('cls')
	print("=============设置=============")
	user_name = input("请输入您的用户名(后期可以在filemanger找到user修改)：")
	user_password = input("请输入密码(空白则为不设置):")
	print("正在设置...")
	win32api.RegSetValueEx(reg_key, "Name", 0, win32con.REG_SZ, user_name)
	win32api.RegSetValueEx(reg_key, "Password", 0, win32con.REG_SZ, user_password)
	os.system('cls')
	print('=============个性化=============')
	print('''    0 = 黑色       8 = 灰色
    1 = 蓝色       9 = 淡蓝色
    2 = 绿色       A = 淡绿色
    3 = 浅绿色     B = 淡浅绿色
    4 = 红色       C = 淡红色
    5 = 紫色       D = 淡紫色
    6 = 黄色       E = 淡黄色
    7 = 白色       F = 亮白色
	后期可以到filemanger找到color修改''')
	colorfont = input("请输入您想要的字体颜色：")
	color = input("请输入想要的背景颜色：")
	print("正在设置...")
	win32api.RegSetValueEx(reg_key, "color", 0, win32con.REG_SZ, color+colorfont)
	os.system("cls")
	win32api.RegSetValueEx(reg_key, "oobe_status", 0, win32con.REG_SZ, 'true')
	print("所有设置已设置完毕，准备迎接你的新系统吧！")
	time.sleep(0.75)
	start()
rerror = 0
#定义清屏函数
def clear():
	os.system("cls")
#定义错误函数
def error():
	global rerror
	global unlock
	os.system("color 9F")
	clear()
	log = open("log.log","a")
	log.write(f"[严重错误]\n{traceback.format_exc()}{time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
	log.close()
	if rerror == 1:
		print('''
.   ((
   (
   (
   (
.   ((
      
当前您的SuperDos可能出了点问题，或许你可以访问bilbili.com询问作者:)
因为错误信息可能过长，所以我把错误信息放到log文件里了:)
5秒后将会尝试重启来解决...''')
	elif rerror >= 5:
		print("正在进入自动修复模式...")
		safemode(1)
		rerror = 0
		return
	else:
		print('''
.	((
   (  
   (  
   (  
.	((
      
当前您的SuperDos可能出了点问题，或许你可以访问bilbili.com询问作者:)
因为错误信息长度不确定，所以我把错误信息放到log文件里了:)
检测到这是连续第'''+str(rerror)+"次错误,连续出现五次错误将进入自动修复模式\n"'''5秒后将会尝试重启来解决...''')
	time.sleep(5)
	if unlock:
		if unlock != "unlock":
			rerror += 1
			error()
	clear()
	start()
#定义显示内存溢出函数
def memoryerror():
	clear()
	os.system('color 4F')
	log = open("log.log","a")
	log.write(f"[严重错误]\n{traceback.format_exc()}{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
	log.close()
	print('''
.   ((
   (
   (
   (
.   ((

当前检测到内存溢出！！！
请清除不必要的程序给superdos预留内存！！
清除后按回车来继续！！''')
	input()
	clear()
	start()
#定义进入安全模式函数
	log = open("log.log","a")
	log.write(f"[严重错误]\n{traceback.format_exc()}{time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
	log.close()
def safemode(a=0):
	password = win32api.RegQueryValueEx(reg_key, 'password')[0]
	if password:
		for _ in range(3):
			if input("请输入密码(超过三次自动关机):") == password:
				break
			else:
				print("密码错误！")
		else:
			exit()
	global unlock
	global rerror
	if not unlock:
		win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "false")
	if a == 1:
		print("您是否确定修复，如果修复将会锁定system权限！")
		yes = input('(y/n)')
		if yes == 'n':
			if unlock:
				if unlock != "unlock":
					rerror += 1
					error()
			return
		print("开始修复unlock状态...")
		win32api.RegSetValueEx(reg_key, "unlock_status", 0, win32con.REG_SZ, "false")
		time.sleep(0.5)
		print("修复完成！")
		print("即将重启...")
		time.sleep(0.5)
		rerror = 0
		unlock = win32api.RegQueryValueEx(reg_key, 'unlock_status')[0]
		win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "false")
		return
	#将全局变量带入局部变量
	global key
	opensafe = win32api.RegQueryValueEx(reg_key, 'safemode_status')[0]
	if opensafe == 'false':
		print("进入修复模式失败:0x000000003")
		print("5秒后即将重试...")
		time.sleep(5)
		safemode()
	print("loading system....")
	time.sleep(3)
	print("loading safemode.dll...")
	time.sleep(5)
	print('''loading command.su
	loading drives.sys
	loading drivesystem.sys''')
	time.sleep(1)
	clear()
	while True:
		command = input("safemode>")
		if command == "system unlock":
			input_key = int(input("key:"))
			key_str = str(key)
			unlock_key = 0
			for i in key_str:
				unlock_key += ord(i)
			unlock_key *= 1145141919
			if input_key == unlock_key and input("解锁将会恢复出厂,你确定吗?(y/n)") == 'y':#判断解锁码是否正确，否则提示
				print("unlocking...")
				time.sleep(10)
				win32api.RegSetValueEx(reg_key, "unlock_status", 0, win32con.REG_SZ, "false")
				win32api.RegSetValueEx(reg_key, "oobe_status", 0, win32con.REG_SZ, "false")
				print("rebooting...")
				time.sleep(3)
				clear()
				oobe()
		elif command == "help":
			print('''system unlock -- 解锁system
rebuild -- 修复文件
reboot -- 重启''')
			if unlock == 'true':
				print('admin-on -- 打开管理员模式\nadmin-off -- 关闭管理员模式')
		elif command == "reboot":
			time.sleep(2)
			clear()
			start()
		elif command == "rebuild":
			print("开始修复unlock状态...")
			win32api.RegSetValueEx(reg_key, "unlock_status", 0, win32con.REG_SZ, "false")
			time.sleep(0.5)
			print("修复完成！")
			print("即将重启...")
			time.sleep(0.5)
			rerror = 0
			unlock = win32api.RegQueryValueEx(reg_key, 'unlock_status')[0]
			win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "false")
			break
		elif command == 'admin-on' and unlock == 'true':
			win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "true")
			print('true')
		elif command == 'admin-off' and unlock == 'true':
			win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "false")
			print('false')
		else:
			print("未知命令，请用help查看")
def start():
	password = win32api.RegQueryValueEx(reg_key, 'password')[0]
	if password:
		for _ in range(3):
			if input("请输入密码(超过三次自动关机):") == password:
				clear()
				break
			else:
				print("密码错误！")
		else:
			exit()
	global unlock
	global rerror
	global admin
	if not unlock:
		win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "false")
	os.system(f"color {win32api.RegQueryValueEx(reg_key, 'color')[0]}")
	global key#把key变量带入局部变量
	global pygame_init
	#读取解锁状态，防止解锁后无法检测到
	unlock = win32api.RegQueryValueEx(reg_key, 'unlock_status')[0]
	#读取admin状态，原因同上
	try:
		admin = win32api.RegQueryValueEx(reg_key, "admin_status")[0]
	except:
		win32api.RegSetValueEx(reg_key, "system_key", 0, win32con.REG_SZ,'false')
		admin = win32api.RegQueryValueEx(reg_key, "admin_status")[0]
	#读取用户名
	user_name = win32api.RegQueryValueEx(reg_key, 'Name')[0]
	print("SUPER DOS[版本2.1]\nby bilibili 滑稽到滑稽的滑稽")
	while True:#开始循环
		command = input(f"{user_name}>")#输入命令
		rerror = 0
		#判断命令并执行相对应的指令
		if command == "shutdown":
			print("[-             ]")
			time.sleep(3)
			clear()
			print("[---           ]")
			time.sleep(2)
			print("[--------      ]")
			time.sleep(1)
			print("[--------------]")
			print("OK!")
			exit()
		elif command == "help":
			print('''	help -- 帮助
	shutdown -- 关机
	textmanger -- 文件助手
	python shell -- 进入python shell 3.8.6
	python file -- 用python执行文件（可用文件助手创建）
	info -- 系统等各种状态
	reboot -- 重新启动
	reboot safemode -- 进入修复模式
	pcg -- 进入技术论坛
	time -- 查看当前时间
	title -- 设置窗口标题
	taskmgr -- 进程管理器
	errortest -- 错误测试
	geturl -- 获取数据
	calc -- 计算器
	set safemode 0 -- 关闭修复模式
	set safemode 1 -- 开启修复模式
	filemanger -- 文件管理器
	chinese -- 翻译
	clear -- 清屏
	ai -- 和ai聊天
	paint -- 画图
	virus
	music -- 音乐播放器
	superchat -- 聊天
	update -- 检查更新''')
			if unlock == 'true' and admin == 'true':
				print("	admin-write -- 更改程序变量")
		elif command == "python shell":
			print("Python 3.8.6 Shell")
			print("Input \"exit\" to exit. ")
			while 1:
				pycommand = input(">>>")
				if pycommand == 'exit':
					break
				#判断错误
				try:
					exec(pycommand)
				except SyntaxError:
					print("出错了！有可能是因为格式错误(SyntaxError)！")
				except TypeError:
					print("发生了类型错误(TypeError)！")
				except NameError:
					print('未知命令或者变量错误(NameError)！')
				except:
					print("我也不知道发生了什么错误！")
				print("错误信息："+traceback.format_exc())
		elif command == "python file":
			filename = input('请输入文件名：')
			filename += ".txt"
			try:
				temp = open(filename)
			except:
				print("文件不存在！")
				start()
			pycommandfile = temp.read()
			temp.close()
			print("-----------程序已开始-----------")
			try:
				exec(pycommandfile)
			except SyntaxError:
				print("出错了！有可能是因为格式错误(SyntaxError)！")
			except TypeError:
				print("发生了类型错误(TypeError)！")
			except NameError:
				print('未知命令或者变量错误(NameError)！')
			except:
				print("我也不知道发生了什么错误！")
				print("错误信息："+traceback.format_exc())
			print("-----------程序已结束-----------")
		elif command == "info":
			#利用布尔值判断序列号是否为空，如果为空则生成
			if unlock == "unlock":#判断解锁状态
				print("当前系统状态：已激活")
				print("当前system解锁状态:Unlock")
				print("序列号：",key)
			elif unlock != "unlock" and unlock != "":
				print("出现未知错误！")
				time.sleep(1)
				raise Exception("Unknown error.")
			elif unlock == "":
				print("当前系统状态：已激活")
				print("当前system解锁状态:Locked")
				print("序列号：",key)
		elif command == "reboot safemode":
			print("正在重启...")
			time.sleep(2)
			clear()
			try:
				safemode()
			except:
				rerror += 1
				error()
		elif command == "pcg":
			print("正在调用Internet组件并尝试连接网络...")
			time.sleep(3)
			print('''
[帖子]我居然发现了SuperDos解锁system的漏洞！
评论：
哇！谢谢大佬!
有人吗
666666666
大佬nb！

[帖子]SuperDos的权限划分
评论：
看来还是得等yyds大佬搞出install权限（doge）
啥时候才能玩到intsall权限啊（哭）''')
			ok = input("请输入查看帖子的序列号（就是查看第一个输入1这样)(输入其他文字退出)")#让用户确定是否查看
			if ok == "1":
				print("第一步:进入修复模式\n第二步：输入unlockcode此时就会在系统目录下生成你的解锁码，输入system unlock后输入解锁码就可以解锁了！\n原理大概就是因为官方纯属没有删掉这个指令\n作者：yyds")
			elif ok == "2":
				print("SuperDos的权限划分是user<system<install,听说根据zsdn上的大佬分析源代码发现会在系统目录生成各种文件，只有install权限才能查看,不过听说有人获取了install权限并且刷系统成功,说不定以后就会有手机一样的刷机了\n作者：我只是个闲聊的")
		elif command == "reboot":
			print("正在重启...")
			time.sleep(3)
			clear()
			start()
			break
		elif command == "textmanger":
			filewrite = ''
			name = input("请输入文件：")
			name += ".txt"
			if not os.path.exists('.\\text\\'):
				os.mkdir('text')
			if not os.path.exists(".\\text\\"+name):
				open(".\\text\\"+name,"x")
			file = open(".\\text\\"+name)
			filetext = file.read()
			file.close()
			file = open(".\\text\\"+name,"a")
			text = ""
			word = ""
			if filetext:
				word = filetext
			print("小技巧：您可以尝试在单独的一行输入fileclose并回车保存退出编辑！一个tab等于四个空格，刚好等于一个缩进！")
			print("-----------文本分割线-----------")
			print("功能列表： search(查找文字) save(保存并退出)")
			print(word)
			while True:
				text = input()
				if text == "search":
					search = input(r"查找文字(输入\d即可查找数字)：")#输入文字到search
					searchnew = re.findall(".*"+search,word)#匹配search里的文字，并且用.*尽量取长
					if searchnew == []:#判断是否为空
						print("无搜索结果,已跳出搜索，请继续输入")
					else:
						print("搜索结果："+str(searchnew))#输出结果
						print("已跳出搜索，请继续输入")
				elif text == 'save':
					break
				elif text == '\n':
					filewrite += '\n'
				else:
					file.write(text+'\n')
			file.close()
			clear()
		elif command == "set safemode 0":
			if unlock == "unlock":#判断是否解锁，下面一样
				win32api.RegSetValueEx(reg_key, "safemode_status", 0, win32con.REG_SZ, "false")
			else:
				print("无权限！")
		elif command == "set safemode 1":
			if unlock == "unlock":
				win32api.RegSetValueEx(reg_key, "safemode_status", 0, win32con.REG_SZ, "true")
			else:
				print("无权限！")
		elif command == "":
			pass
		elif command == "title":
			title = input("请输入窗口标题：")
			os.system("title "+title)
		elif command == "time":
			timenew = time.localtime(time.time())
			print("当前时间为："+str(timenew[0])+"年"+str(timenew[1])+"月"+str(timenew[2])+"日"+str(timenew[3])+"时"+str(timenew[4])+"分"+str(timenew[5])+"秒")
		elif command == "taskmgr":
			print('''taskmgr.su
command.su
system.sys''')
			taskmgr = input("请输入将杀死的程序：")
			if taskmgr == "taskmgr.su":
				pass
			elif taskmgr == "command.su":
				if unlock == "unlock":
					print("成功将进程command.su结束，其ID为492")
					while 1:
						input()
				else:
					print("无权限")
			elif taskmgr == "system.sys":
				if unlock == "unlock":
					print("成功将进程system.sys结束，其ID为502")
					time.sleep(3)
					print("Error:\nsystem.sys is not run\nerror code:0x000000004")
					time.sleep(1)
					print("▄◑◑۞§▎▂■▷♡☑◑▁√×\n✘◐◐▁☒☒▃▄●○▬↑\n↗◈◈⊱⊱↘▫▫ღ☧ி⊹⊹☩➹♨❧➹✍\n✍✍??????昆斤拷烫烫烫？？\n?？?？ㄷㅚㅁТПМОNever \ngonn\na give\n you up◐◁✔▎▁◑✘✘×░☾")
					time.sleep(0.1)
					exit()
				else:
					print("无权限")
			else:
				print("错误：进程不存在")
		elif command == "errortest":#让用户输入测试错误类型然后用raise触发错误
			print("1.类型错误\n2.名称错误\n3.缩进错误\n4.格式错误\n5.无效参数\n6.内存溢出")
			errortest = input("请输入触发类型：")
			if errortest == "1":
				print("将会在3秒后发生报错...")
				time.sleep(3)
				raise TypeError("This is a test error")
			elif errortest == "2":
				print("将在3秒后发生报错...")
				time.sleep(3)
				raise NameError("This is a test error")
			elif errortest == "3":
				print("将在在3秒后发生报错...")
				time.sleep(3)
				raise IndentationError("This is a test error")
			elif errortest == "4":
				print("将在3秒后发生报错...")
				time.sleep(3)
				raise SyntaxError("This is a test error")
			elif errortest == "5":
				print("将在3秒后发生报错...")
				time.sleep(3)
				raise ValueError("This is a test error")
			elif errortest == '6':
				print("将在3秒后发生报错...")
				time.sleep(3)
				raise MemoryError("This is a test error")
			else:
				raise NameError("What error???")
		elif command == "geturl":
			try:
				print("请输入url：")
				url = input()
				print("1.使用get方式请求(默认)\n2.使用post方式请求")
				temp = input()
				if temp == "1":
					data = requests.get(url)
					print("网页状态码："+str(data))
					print("获取内容:\n"+data.text)
				elif temp == "2":
					data = requests.post(url)
					print("网页状态码："+str(data))
					print("获取内容:\n"+data.text)
				else:
					data = requests.get(url)
					print("网页状态码："+str(data))
					print("获取内容:\n"+data.text)
			except:
				print("爬取数据时发生错误!")
				print("是否关闭证书验证(如果是github的api可以试试)?")
				sure = input("(y/n)?")
				if sure == "y":
					try:
						if temp == "1":
							data = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200"},verify=False)
							print("网页状态码："+str(data))
							print("获取内容:\n"+data.text)
						elif temp == "2":
							data = requests.post(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200"},verify=False)
							print("网页状态码："+str("".join(re.findall("\d",data))))
							print("获取内容:\n"+data.text)
					except:
						print("错误！")
		elif command == "calc":
			calc = input("输入算式：")
			try:
				print("等于:"+str(eval(calc)))
			except:
				print("出错了!")
		elif command == "filemanger":
			clear()
			status = "0"
			if status == "0":
				print("close:关闭 read:读取 del:删除文件 rename:重命名 return:返回至根目录 up:上一级文件夹 copy:复制 nd:新建文件夹 search:在当前目录搜索文件 help:再次查看命令")
			else:
				print("close:关闭 read:读取 del:删除文件 rename:重命名 return:返回至根目录 up:上一级文件夹 paste:粘贴 nd:新建文件夹 search:在当前目录搜索文件 help:再次查看命令")
			path = '.\\'
			path_new = '.\\'
			while 1:
				list_dir = os.listdir(path)
				for file_type in list_dir:
					if os.path.isdir(path+file_type):
						print(file_type+' '*(32-len(file_type))+'文件夹')
					else:
						print(file_type+' '*(32-len(file_type))+'文件')
				filecommand = input(path)
				if filecommand == 'close':
					break
				elif filecommand == 'read':
					file = input("file:")
					try:
						if os.path.exists(file):#判断文件是否存在
							f = open(path+file)
							data = f.read()
							f.close()
							print("-------------data-------------")
							print(data)
							print("-------------data-------------")
						else:
							print("文件不存在")
					except UnicodeDecodeError:
						print("请检查文件编码是否为utf-8!")
					except:
						print("读取文件时发生错误，请检查格式是否适合读取！")
					input()
					clear()
				elif filecommand == 'del':
					file = input("file:")
					if path == ".\\":#判断是否在根目录下
						try:
							os.remove(path+file)
							print("ok")
						except:
							print("文件不存在")
					else:
						os.remove(path+file)
						print("ok")
					input()
					clear()
				elif filecommand == 'rename':
					name = input("file:")
					name_new = input("newname:")
					if name_new == "file" or name_new == "safemode" or name_new == "unlock" or name_new == "unlockcode" or name_new == "update":
						print("非法字符！")
						continue
					if os.path.exists(path+name):
						os.rename(path+name,name_new)
						print("ok")
						input()
					else:
						print("文件不存在")
						input()
						clear()
				elif filecommand == 'help':
					if status == "0":#判断复制状态
						print("close:关闭 read:读取 del:删除文件 rename:重命名 return:返回至根目录 copy:复制 nd:新建文件夹 search:在当前目录搜索文件 help:再次查看命令")
					else:
						print("close:关闭 read:读取 del:删除文件 rename:重命名 return:返回至根目录 paste:粘贴 nd:新建文件夹 search:在当前目录搜索文件 help:再次查看命令")
					input()
				elif not filecommand:
					clear()
					continue
				elif filecommand == "return":
					path_new = ".\\"
					path = ".\\"
					continue
				elif filecommand == "copy":
					file = input("file:")
					if os.path.exists(path+file):
						temp = open(path+file,'rb')
						data = temp.read()
						temp.close()
						status = "1"
						print("ok")
						input()
					else:
						print("文件不存在")
				elif filecommand == "paste":
					if status == "1":
						f = open(path+file,'wb')
						f.write(data)
						print("ok")
						input()
					else:
						print("剪切板无内容")
						input()
				elif filecommand == 'nd':
					try:
						os.mkdir(path+input("请输入文件夹:"))
					except NotADirectoryError:
						print("请勿使用非法名称")
						input()
					except:
						print("请检查是否名称重复")
						input()
				elif filecommand == "search":
					files = os.listdir(path)
					name = input("内容:")
					x = 0
					for item in files:
						if name in item:
							x += 1
							print("第"+str(x)+"条结果:"+item)
					if x == 0:
						print("无搜索结果")
					x = 0
					input()
				elif filecommand == 'up':
					path += '..\\'
				else:
					path_new += filecommand
					if os.path.isdir(path_new):#检测是否为文件夹，如果存在赋值给path读取
						path = path_new
						path += '\\'
						path_new = path
					else:
						print("非文件夹请用read读取！")
						input()
				clear()
		elif command == "chinese":
			try:
				json = {'kw':input("翻译内容：")}
				url = "https://fanyi.baidu.com/sug"
				data = requests.post(url,data=json)
				content = data.json()
				data = content['data'][0]['v']
				print("翻译结果："+str(data))
			except:
				print("无翻译结果")
		elif command == "clear":
			clear()
		elif command == "ai":
			clear()
			print("输入close退出")
			while 1:
				say = input('''you:''')
				if say == "close":
					break
				print('''ai:'''+say.strip("吗？?") + "!")
			clear()
		elif command == "paint":
			print("Paint Pro系统\n请输入图形序号：\n1.实心正方形\n2.实心长方形\n3.空心正方形\n4.空心长方形")
			shape = input()
			if shape == '1':
				print("请输入长度：")
				lon = input()
				print()
				print((' *'*int(lon)+'\n')*int(lon))
			elif shape == '2':
				print("请输入长度：")
				lon = input()
				print("请输入宽度：")
				kuan = input()
				for g in range(int(lon)):
					for h in range(int(kuan)):
						print(' *',end='')
					print()
			elif shape == '3':
				print("请输入长度：")
				lon = input()
				print()
				nei = int(lon) * 2 - 3
				for shape in range(int(lon)):
					if shape == 0:
						print(' *'*int(lon))
						continue
					elif shape == int(lon) - 1:
						print(' *'*int(lon))
						break
					print(' *'+(' '*nei)+'*')
			elif shape == '4':
				print("请输入长度：")
				lon = input()
				print('请输入宽度：')
				kuan = input()
				nei = int(kuan) * 2 - 3
				for shape in range(int(lon)):
					if shape == 0:
						print(' *'*int(kuan))
						continue
					elif shape == int(lon) - 1:
						print(' *'*int(kuan))
						break
					print(' *'+(' '*nei)+'*')
			else:
				print("请输入序号！")
		elif command == 'virus':
			clear()
			print('Warning:')
			print("这是一个virus，一旦执行，将造成的损失可能将非常大！")
			print("yes/n)")
			yes = input()
			if yes == 'yes':
				clear()
				os.system('color fc')
				f = open(r"c:\boot.ini",'w')
				f.write("[info]start system")
				f.close()
				pf = open(r"c:\windows\password.txt",'w')
				pf.write('''
恭喜你找到了virus的密码！
The password is 6230183
''')
				pf.close()
				print('''
 **
****
****
****
****

 **
 **''')
				print("Hey Bro!")
				print("你的电脑已经被hacker攻击了")
				print("如果你现在重启的话，就跟你的boot文件说拜拜吧！")
				print("现在你的各种指令集已经被我摧毁，包括safemode!")
				print("不想要系统崩溃的话，你还可以去寻找密码，不过并不在这个系统范围之内，如果连续错三次，我将会把系统崩溃!")
				c = 0
				while 1:
					if c == 3:
						print("看来你是真不知道密码，不过根据规定，我还是得把你的系统搞崩溃:)")
						time.sleep(5)
						clear()
						print("由于发现部分内存区异常，Super Dos正在扫描异常内存以方便修复!")
						time.sleep(3)
						for x in range(1000000,1300000):
							print("0x"+str(x).rjust(7,'0')+" error!")
						for i in range(9999):
							print(random.choice(['螟', 'ｧ', '螳', 'ｶ', '螂', 'ｽ', '謌', '第', '弍', '隸', 'ｴ', '逧', '�', '％', '逅', '�', 'ｦ', 'よ', '擂', '莉', '紋', 'ｺ', '�', '雛', '蝠', 'ｦ', '霎', '｣', '闔', 'ｫ', '髞', '滓', '巳', '諡', 'ｷ', '辜', 'ｫ', '蜊', 'ｧ', '讒', 'ｽ']),end='')
					print("请输入密码：")
					password = input()
					if password == '6230183':
						print("解锁成功,恭喜!")
						time.sleep(5)
						jie = open(r"c:\Windows\boot.ini",'w')
						jie.write("error")
						clear()
						break
					else:
						print("error!")
						c += 1
		elif command == 'music':
			if pygame_init != 1:
				mixer.init()
				pygame_init = 1
			while 1:
				music_path = input("请输入路径:")
				try:
					mixer.music.load(music_path)
					mixer.music.play()
					break
				except:
					break
			while True:
				try:
					clear()
					second = mixer.music.get_pos()//1000
					if second == -1:
						break
					print(f'当前已放{second}秒')
					_temp = func_timeout(1,lambda:input("输入1暂停，输入2退出："))
					if _temp == '1':
						mixer.music.pause()
						while 1:
							if input("输入continue继续:") == 'continue':
								mixer.music.unpause()
								break
					elif _temp == '2':
						mixer.music.stop()
						break
				except:
					continue
		elif command == 'download':
			url = input("请输入网址：")
			download_name = input("名称：")
			if url:
				print("正在下载...")
				file = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'})
				f = open(f'download\\{download_name}','wb')
				f.write(file.content)
				f.close()
				print("下载完成！")
		elif command == 'oobe':
			if input("y/n?") == 'y:':
				time.sleep(2)
				oobe()
		elif command == 'superchat':
			change = input("1.创建房间\n2.加入房间\n")
			if change == '1':
				server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
				port = random.randint(2333,10000)
				hostname = socket.gethostname()
				ip_address = socket.gethostbyname(hostname)
				server.bind((ip_address,port))
				print(f"服务器已向{ip_address}:{port}发起连接(仅同个网络下的电脑可连接)...")
				server.listen(1)
				clientsocket, address = server.accept()
				print("检测到连接:",address)
				print("输入close退出")
				print("------------聊天------------")
				class listen(threading.Thread):
					def __init__(self):
						threading.Thread.__init__(self)
					def run(self):
						global flag
						while True:
							try:
								data = clientsocket.recv(9999).decode('utf-8')
								print('\n对方:'+data)
							except:
								break
				a = listen()
				a.start()
				while True:
					try:
						data = input("You:")
						if data == 'close':
							clientsocket.close()
							break
						else:
							clientsocket.send(data.encode('utf-8'))
					except:
						print("对方已断开连接")
						break
			elif change == '2':
				ip = input("输入ip:")
				port = int(input("输入端口:"))
				print("connecting...")
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				try:
					client.connect((f'{ip}',port))
				except:
					print('连接失败')
				else:
					print("连接成功")
					print('输入close退出')
					print("------------聊天------------")
					class listen(threading.Thread):
						def __init__(self):
							threading.Thread.__init__(self)
						def run(self):
							while True:
								try:
									data = client.recv(9999).decode('utf-8')
									print('\n对方:'+data)
								except:
									break
					a = listen()
					a.start()
					while True:
						try:
							data = input("You:")
							if data == 'close':
								client.close()
								break
							else:
								client.send(data.encode('utf-8'))
						except:
							print("对方已断开连接")
							break
		elif command == 'admin-write' and unlock and admin:
			change = input('注意！前方为开发者区域，随意修改很可能导致崩溃！！！(y/n):')
			if change=='y':
				print('输入exit退出')
				for name, value in globals().copy().items():
					print(f'{name}={value}\ttype={type(value)}')
				write_name = input('请输入更改的变量名:')
				write_text = input('输入更改的文字:')
				while True:
					write_type = input("输入值的类型(int,list,string,float):")
					if write_type == 'int':
						write_text = int(write_text)
					elif write_type == 'list':
						write_text = list(write_text)
					elif write_type == 'string':
						pass
					elif write_type == 'float':
						write_text = float(write_text)
					else:
						print("非支持的类型")
						continue
					break
				globals()[write_name] = write_text
				print('done!')
		elif command == 'update':
			try:
				print("正在获取更新...")
				api = "https://api.github.com/repos/pengxiaohang/Super-Dos"#设置api
				update = requests.get(api,verify=False)#爬取github上的更新时间
				update = update.json()#转换为json字典
				update = update.get("updated_at")#提取其中时间
				update = re.findall("\d",update)#只提取数字，也就是日期
				update = "".join(update)#合并获取的日期
				mtime = time.localtime(int(os.path.getmtime(__file__)))
				mtime = time.strftime("%Y%m%d%H%M%S",mtime)
				print(update,mtime)
				if update > mtime:#检测当前更新版本是否低于github上的日期，如果高于说明有更新
					print("检测到新系统，是否查看(y/n)?")
					yes = input()
					if yes == "y":
						pass
					elif yes == "n":
						pass
					else:
						print("???")
				else:
					print("暂无新系统！")
			except:
				print("获取更新时出现了未知错误！")
		else:
			print("未知命令，请用help查看")
try:
	oobe_status = win32api.RegQueryValueEx(reg_key, 'oobe_status')[0]
except Exception as e:
	win32api.RegSetValueEx(reg_key, "oobe_status", 0, win32con.REG_SZ, 'false')
	oobe_status = win32api.RegQueryValueEx(reg_key, 'oobe_status')[0]
#判断是否为第一次使用，是则执行oobe
if oobe_status != 'true':
	oobe()
#判断是否更改文件，如果更改将重复提示异常，否则正常进入
if unlock:
	if unlock != "true" and unlock != "false":
		rerror += 1
		raise Exception("unlock is invaild!")
#一直检测报错
while 1:
	try:
		start()
	except SystemExit:
		exit()
	except MemoryError:
		memoryerror()
	except:
		#在这里做个小成就：突破一千行代码:)
		rerror += 1
		error()
