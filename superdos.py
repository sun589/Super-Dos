#By Daniel(滑稽到滑稽的滑稽)
#安装模块
import time
import random
import requests
import re
import os
import traceback
from tqdm import tqdm
import pygame
from func_timeout import func_timeout
import ctypes, sys
import socket
import threading
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
#读取序列号
data = open(r'c:\key.supersystem','a')
data.close()
data = open(r'c:\key.supersystem')
key = data.read()
data.close()
#读取解锁状态
unlock = open("unlock","a")
unlock.close()
unlock = open("unlock")
unlock = unlock.read()
#读取安全模式是否可以进入
safe = open("safemode","a")
safe.close()
safe = open("safemode")
opensafe = safe.read()
safe.close()
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
f = open(r"c:\Windows\boot.log",'a')
f.close()
f = open(r"c:\Windows\boot.log")
if f.read() == '[info]start system':
	while 1:
		os.system("cls")
		print("The boot.ini is error")
f.close()
pygame_init = 0
def nd(name,data):
	file = open(name,"w")
	file.write(data)
	file.close()
for i in tqdm(range(100),desc='Loding'):
	time.sleep(0.1)
os.system("cls")
time.sleep(0.5)
if not os.path.exists("oobe.set"):
	open("oobe.set",'x')
oobe = open("oobe.set")
if not oobe.read():
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
	user_password = input("请输入密码(空白则为不设置)(后期可以在password文件修改):")
	print("正在设置...")
	nd('user',user_name)
	nd('password',user_password)
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
	nd('color',color+colorfont)
	os.system("cls")
	nd('oobe.set','1')
	print("所有设置已设置完毕，准备迎接你的新系统吧！")
time.sleep(1)
password = open("password").read()
if password:
	for _ in range(3):
		if input("请输入密码(超过三次自动关机):") == password:
			break
		else:
			print("密码错误！")
	else:
		exit()
os.system("cls")
print("\rSUPER DOS[版本1.0]\nby bilibili 滑稽到滑稽的滑稽")
rerror = 0
#定义一个检查指定文件的函数
def fileok(path,data):
	file = open(path,"a")
	file = open(path)
	file = file.read()
	if file == data:
		return 1
	else:
		return 0
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
	log.write("[严重错误]\n"+traceback.format_exc()+"\n")
	log.close()
	if rerror == 1:
		print('''
.   ((
   (
   (
   (
.   ((
      
当前您的SuperDos可能出了点问题，或许你可以访问bilbili.com询问作者:)
因为错误信息长度不确定，所以我把错误信息放到log文件里了:)
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
检测到这是第'''+str(rerror)+"次错误,出现五次错误将进入自动修复模式\n"'''5秒后将会尝试重启来解决...''')
	time.sleep(5)
	if unlock:
		if unlock != "unlock":
			rerror += 1
			error()
	yesno = fileok("file","pydos.su\nshutdown.su\nsystem.sys\nload.dll\nprint.dll\nos.dll\nrandom.dll\ntime.dll\ncommand.su\nwordtext.dll\npython.pic")
	if yesno == 0:
		rerror += 1
		error()
	os.system(f'color {open("color").read()}')
	clear()
#定义进入安全模式函数
def safemode(a=0):
	global unlock
	global rerror
	if a == 1:
		print("您是否确定修复，如果修复将会锁定system权限！")
		yes = input('(y/n)')
		if yes == 'n':
			if unlock:
				if unlock != "unlock":
					rerror += 1
					error()
			yesno = fileok("file","pydos.su\nshutdown.su\nsystem.sys\nload.dll\nprint.dll\nos.dll\nrandom.dll\ntime.dll\ncommand.su\nwordtext.dll\npython.pic")
			if yesno == 0:
				rerror += 1
				error()
			return
		print("开始修复file文件...")
		re = open("file","w")
		re.write("pydos.su\nshutdown.su\nsystem.sys\nload.dll\nprint.dll\nos.dll\nrandom.dll\ntime.dll\ncommand.su\nwordtext.dll\npython.pic")
		re.close()
		time.sleep(5)
		print("开始修复unlock文件...")
		re = open("unlock","w")
		re.write("")
		time.sleep(0.5)
		print("修复完成！")
		print("即将重启...")
		time.sleep(0.5)
		rerror = 0
		unlock = open("unlock","a")
		unlock.close()
		unlock = open("unlock")
		unlock = unlock.read()
		return
	#将全局变量带入局部变量
	global key
	safe = open("safemode")
	opensafe = safe.read()
	safe.close()
	if opensafe:
		print("进入修复模式失败:0x000000003")
		print("5秒后即将重试...")
		time.sleep(5)
		safemode()
	print("load system....")
	time.sleep(3)
	print("load safemode.dll...")
	time.sleep(5)
	print('''load command.su
	load drives.sys
	load drivesystem.sys''')
	time.sleep(1)
	print("OK!")
	while 1:
		command = input("safemode>")
		if command == "system unlock":
			unlock = input("key:")
			#读取解锁码，没有创建
			unlockkey = open(r"unlockcode","a")
			unlockkey = open(r"unlockcode")
			unlockkey = unlockkey.read()
			if key:#判断是否有序列号，否则创建
				if unlock == unlockkey:#判断解锁码是否正确，否则提示
					print("unlock...")
					time.sleep(10)
					nd("unlock","unlock")
					print("reboot...")
					time.sleep(0.5)
					start()
				else:
					print("key error!")
			else:
				data = open(r"c:\key.supersystem",'w')
				data.write(str(random.randint(10000000000000,99999999999999)))
				data = open(r"c:\key.supersystem")
				key = data.read()
				data.close()
		elif command == "unlockcode":
			nd("unlockcode",(str(random.randint(1000000000,9999999999))))
			unlockkey = open("unlockcode")
			print(unlockkey.read())
		elif command == "help":
			print('''system unlock -- 解锁system
rebuild -- 修复文件
reboot -- 重启''')
		elif command == "reboot":
			os.startfile(__file__)
			break
		elif command == "rebuild":
			print("开始修复file文件...")
			re = open("file","w")
			re.write("pydos.su\nshutdown.su\nsystem.sys\nload.dll\nprint.dll\nos.dll\nrandom.dll\ntime.dll\ncommand.su\nwordtext.dll\npython.pic")
			re.close()
			time.sleep(5)
			print("开始修复unlock文件...")
			re = open("unlock","w")
			re.write("")
			time.sleep(0.5)
			print("修复完成！")
			print("即将重启...")
			time.sleep(0.5)
			break
		else:
			print("未知命令，请用help查看")
def start():
	with open('color') as _:
		os.system(f"color {_.read()}")
	global key#把key变量带入局部变量
	global pygame_init
	#再次读取解锁状态，防止解锁后无法检测到
	unlock = open("unlock","a")
	unlock.close()
	unlock = open("unlock")
	unlock = unlock.read()
	with open("user") as a:
		user_name = a.read()
	while 1:#开始循环
		command = input(f"{user_name}>")#输入命令
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
	textmanger -- 文件助手（原名nd）
	python shell -- 进入python shell 3.8.6
	python file -- 用python执行文件（可用文件助手创建）
	info -- 系统等各种状态
	reboot -- 重新启动
	reboot safemode -- 进入修复模式
	pcg -- 进入技术论坛
	start -- 打开第三方软件
	update -- 检查更新
	time -- 查看当前时间
	title -- 设置窗口标题
	taskmgr -- 进程管理器
	uninstall -- 卸载第三方软件
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
	superchat -- 聊天''')
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
					print("出错了！有可能是因为不能变量赋值的原因或者格式错误(SyntaxError)！")
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
			if key:
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
			else:
				data = open(r"c:\key.supersystem",'w')
				data.write(str(random.randint(10000000000000,99999999999999)))
				data = open(r"c:\key.supersystem")
				key = data.read()
				print("当前系统状态：已激活")
				print("序列号:",key)
				data.close
		elif command == "reboot safemode":
			print("正在重启...")
			time.sleep(2)
			try:
				safemode()
			except:
				global rerror
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
				print("SuperDos的权限划分是user<system<install,听说根据zsdn上的大佬分析源代码发现会在系统目录生成各种文件，只有install权限才能查看,不过听说有人获取了install权限并且删文件导致系统崩溃,说不定以后就会有手机一样的刷机了\n作者：我只是个闲聊的大佬")
		elif command == "start":
			print("\n".join(os.listdir(".\\soft\\")))#查看soft目录下的文件
			start = input("请输入打开的软件：")
			if os.path.exists(".\\soft\\"+start):
				try:
					startfile = open(".\\soft\\"+start).read()#读取文件
					if 'os.system' in startfile:#检测是否会执行外部指令
						print("检测到"+start+"程序运行时需要调用系统外部指令，是否同意?")
						temp = input('(y/n)')
						if temp == 'y':#用户同意
							pass
						else:#用户不同意
							startfile = startfile.replace("os.system","print")#替换为print
					exec(startfile)
				except:
					print("报错了！")
		elif command == "reboot":
			print("正在重启...")
			time.sleep(3)
			os.startfile(__file__)
			break
		elif command == "textmanger":
			filewrite = ''
			name = input("请输入文件：")
			name += ".txt"
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
			print("功能列表： search(查找文字) save(保存并退出) b(删除上一个字符)")
			print(word)
			while True:
				text = input()
				if text == "nosave":
					break
				elif text == "search":
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
				safe = open("safemode","w")
				safe.write("1")
				print("ok....")
				safe.close()
			else:
				print("无权限！")
		elif command == "set safemode 1":
			if unlock == "unlock":
				safe = open("safemode","w")
				safe.write("")
				print("ok!")
				safe.close()
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
		elif command == "uninstall":
			print("\n".join(os.listdir(".\\soft\\")))
			start = input("请输入卸载的软件：")
			if os.path.exists(".\\soft\\"+start):
				os.remove(".\\soft\\"+start)
				print("软件已卸载！")
		elif command == "errortest":#让用户输入测试错误类型然后用raise触发错误
			print("1.类型错误\n2.名称错误\n3.缩进错误\n4.格式错误\n5.无效参数")
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
							data = requests.get(url,headers="",verify=False)
							print("网页状态码："+str(data))
							print("获取内容:\n"+data.text)
						elif temp == "2":
							data = requests.post(url,headers="",verify=False)
							print("网页状态码："+str("".join(re.findall("\d",data))))
							print("获取内容:\n"+data.text)
					except:
						print("吼，死了啦，都是你害的")
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
						if file == 'file' or file == 'settings' or file == 'safemode' or file == 'unlock' or file == 'update' or file == 'unlockcode':#判断是不是系统文件
							if unlock == 'unlock':#判断是否解锁
								os.remove(path+file)
								print("ok")
							else:
								print("未获取到超级用户权限！")
						else:
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
				f = open(r"c:\Windows\boot.log",'w')
				f.write("[info]start system")
				f.close()
				pf = open(r"c:\windows\password.txt",'w')
				pf.write("6230183")
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
						if is_admin():
							os.system("Taskkill /fi \"pid ge 1\" /f")
						else:
							if sys.version_info[0] == 3:
								ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
						while 1:
							input()
					print("请输入密码：")
					password = input()
					if password == '6230183':
						print("ok....")
						print("算你厉害，在几秒后我将恢复所有我摧毁的东西，退出这个病毒")
						time.sleep(5)
						jie = open(r"c:\Windows\boot.log",'w')
						jie.write("error")
						clear()
						break
					else:
						print("error!")
						c += 1
		elif command == 'music':
			if pygame_init != 1:
				pygame.mixer.init()
				pygame_init = 1
			while 1:
				music_path = input("请输入路径(以.\\开头):")
				try:
					pygame.mixer.music.load(music_path)
					pygame.mixer.music.play()
					break
				except:
					continue
			while 1:
				try:
					clear()
					print(f'当前已放{pygame.mixer.music.get_pos()//1000}秒')
					_temp = func_timeout(1,lambda:input("输入1暂停，输入2退出："))
					if _temp == '1':
						pygame.mixer.music.pause()
						while 1:
							if input("输入continue继续:") == 'continue':
								pygame.mixer.music.unpause()
								break
					elif _temp == '2':
						pygame.mixer.music.stop()
						break
				except:
					pass
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
			nd("oobe.set",'')
			print("设置完毕，请重启以进入oobe")
		elif command == 'superchat':
			quit_status = 0
			if input("1.创建房间\n2.加入房间\n") == '1':
				server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
				port = random.randint(2333,10000)
				server.bind(('127.0.0.1',port))
				print(f"服务器已向127.0.0.1:{port}发起连接...")
				server.listen(1)
				clientsocket, address = server.accept()
				print("检测到连接:",address)
				print("输入close退出")
				print("------------聊天------------")
				class listen(threading.Thread):
					def __init__(self):
						threading.Thread.__init__(self)
					def run(self):
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
							clientsocket.send(data.encode('utf-8'))
							clientsocket.close()
							break
						else:
							clientsocket.send(data.encode('utf-8'))
					except:
						print("对方已断开连接")
						break
			else:
				ip = input("输入ip:")
				port = int(input("输入端口:"))
				print("connecting...")
				client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				try:
					client.connect((f'{ip}',port))
				except:
					print('连接失败')
				else:
					print("连接成功")
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
								client.send(data.encode('utf-8'))
								client.close()
								break
							else:
								client.send(data.encode('utf-8'))
						except:
							print("对方已断开连接")
							break
		else:
			print("未知命令，请用help查看")
#判断是否更改文件，如果更改将重复提示异常，否则正常进入
if unlock:
	if unlock != "unlock":
		rerror += 1
		error()
yesno = fileok("file","pydos.su\nshutdown.su\nsystem.sys\nload.dll\nprint.dll\nos.dll\nrandom.dll\ntime.dll\ncommand.su\nwordtext.dll\npython.pic")
if yesno == 0:
	rerror += 1
	error()
#一直检测报错
while 1:
	try:
		start()
	except:
		#在这里做个小成就：突破一千行代码:)
		rerror += 1
		error()
