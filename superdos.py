#安装模块
import time
import random
import requests
import re
import webbrowser
import os
#更改窗口名称
os.system("title Super Dos")
#模拟加载
print("328KB OK")
time.sleep(3)
print("625KB OK")
time.sleep(1)
print("1024KB OK")
time.sleep(0.5)
print("cpu:antel s9 10002K")
print("gpu:stx 4090ti")
print("ram:1024KB")
time.sleep(1)
print("SUPER DOS[版本1.0]\nby bilibili 滑稽到滑稽的滑稽")
#定义一个创建文件的函数
def nd(name,data):
	file = open(name,"w")
	file.write(data)
#定义一个检查指定文件的函数
def fileok(name,data):
	file = open(name,"a")
	file = open(name)
	file = file.read()
	if file == data:
		return 1
	else:
		return 0
#读取序列号
data = open(r'c:\key.supersystem','a')
data = open(r'c:\key.supersystem')
key = data.read()
data.close
#读取解锁状态
unlock = open("unlock","a")
unlock.close
unlock = open("unlock")
unlock = unlock.read()
#读取更新状态
file = open("update","a")
file.close
file = open("update")
upsoft = file.read()
file.close
#定义进入安全模式函数
def safemode():
	global key#将全局变量带入局部变量
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
				data.close
		elif command == "unlockcode":
			nd("unlockcode",(str(random.randint(1000000000,9999999999))))
			unlockkey = open("unlockcode")
			print(unlockkey)
		elif command == "help":
			print('''system unlock -- 解锁system
reboot -- 重启''')
		elif command == "reboot":
			start()
def start():
	global key#把key变量带入局部变量
	#再次读取解锁状态，防止解锁后无法检测到
	unlock = open("unlock","a")
	unlock.close
	unlock = open("unlock")
	unlock = unlock.read()
	while 1:#开始循环
		command = input(r"A:\sdos\user>")#输入命令
		#判断命令并执行相对应的指令
		if command == "shutdown":
			print("[-             ]")
			time.sleep(3)
			print("[---           ]")
			time.sleep(2)
			print("[--------      ]")
			time.sleep(1)
			print("[--------------]")
			print("OK!")
			break
		elif command == "help":
			print('''	help -- 帮助
	shutdown -- 关机
	nd -- 创建新文件
	python -- 执行python命令
	dir -- 查看当前目录下的文件
	info -- 系统等各种状态
	reboot -- 重新启动
	reboot safemode -- 进入修复模式
	pcg -- 进入技术论坛(因为用到最新开发的网络，所以还是测试版本)
	start -- 执行指定文件
	reupd -- 更新更新状态（更新了之后用，可以跳过版本提示）''')
		elif command == "nd":
			name = input("请输入文件名字：")
			name = name + ".superdos"
			data = input("请输入内容，因为技术原因无法换行：")
			nd(name,data)
			print("OK!")
		elif command == "python":
			pycommand = input("请输入python命令(无法换行）：")
			#判断错误
			try:
				eval(pycommand)
			except SyntaxError:
				print("出错了！有可能是因为不能变量赋值的原因或者格式错误(SyntaxError)！")
			except TypeError:
				print("发生了类型错误(TypeError)！")
			except NameError:
				print('未知命令或者变量错误(NameError)！')
			except IndentationError:
				print("爷的缩进呢(IndentationError)？？？")
			except:
				print("我也不知道发生了什么错误！也有可能是这个指令做不了的事情！")
		elif command == "dir":
			#读取列表
			file = open("file","a")
			file.close
			file = open("file")
			data = file.read()
			#判断是否有文件，没有创建
			if data:
				file = open("file")
				data = file.read()
				print(data)
			else:
				file.close
				file = open("file","w")
				file.write("pydos.su\nshutdown.su\nsystem.sys\nload.dll\nprint.dll\nos.dll\nrandom.dll\ntime.dll\ncommand.su\nwordtext.dll\npython.pic")
				file.close
				file = open("file")
				data = file.read()
				print(data)
				file.close
		elif command == "info":
			#利用布尔值判断序列号是否为空，如果为空则生成
			if key:
				print("当前系统状态：已激活")
				if unlock == "unlock":#判断解锁状态
					print("当前system解锁状态:Unlock")
					print("序列号：",key)
				else:
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
			boot = 1#让boot变量设置为1，这样就可以进入修复模式
			print("正在重启...")
			time.sleep(2)
			safemode()#调用safemode函数
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
			#读取文件，没有创建
			file = open("file","a")
			file.close
			file = open("file")
			data = file.read()
			if data:#检测文字是否为空，空则填充
				file = open("file")
				data = file.read()
				print(data)
			else:
				file.close
				file = open("file","w")
				file.write("pydos.su\nshutdown.su\nsystem.sys\nload.dll\nprint.dll\nos.dll\nrandom.dll\ntime.dll\ncommand.su\nwordtext.dll\npython.pic")
				file.close
				file = open("file")
				data = file.read()
				print(data)
				file.close
			file = input("请输入文件名(包含后缀):")
			if file == "python.pic":
				open("python.jpg")
			else:
				if unlock == "unlock":
					p = "0"
					for i in range(21):
						p += str(random.randint(0,1))
						print(p,end="")
					print()
				else:
					print("当前区域为system区，需要解锁system，只可以打开图片查看！")
		elif command == "reboot":
			print("正在重启...")
			time.sleep(3)
			print("OK!")
			start()
		elif command == "update":
			try:
				print("正在获取更新...")
				api = "https://api.github.com/repos/pengxiaohang/Super-Dos"#设置api
				update = requests.get(api,headers="",verify=False)#爬取github上的更新时间
				update = update.json()#转换为json字典
				update = update.get("updated_at")#提取其中时间
				update = re.findall("\d",update)#只提取数字，也就是日期
				update = "".join(update)#合并获取的日期
				if update > upsoft:#检测当前更新版本是否低于github上的日期，如果高于说明有更新
					print("检测到新系统，是否查看(y/n)?")
					yes = input()
					if yes == "y":
						webbrowser.open("https://github.com/pengxiaohang/Super-Dos/releases")
					elif yes == "n":
						pass
					else:
						print("???")
				else:
					print("暂无新系统！")
			except:
				print("获取更新时出现了未知错误！")
		elif command == "reupd":
			#获取当前时间戳并转换生成到time_tuple列表
			time_tuple = time.localtime(time.time())
			#把列表指定的元素提取并判断是不是两位数，如果是则在左边补0
			time_tuple3 = time_tuple[3]
			time_tuple3 -= 12
			time_tuple3 = str(time_tuple3)
			if int(time_tuple3) < 10:
				time_tuple3 = time_tuple3.rjust(2,"0")
			time_tuple1 = time_tuple[1]
			time_tuple1 = str(time_tuple1)
			if int(time_tuple1) < 10:
				time_tuple1 = time_tuple1.rjust(2,"0")
			time_tuple2 = time_tuple[2]
			time_tuple2 = str(time_tuple2)
			if int(time_tuple2) < 10:
				time_tuple2 = time_tuple2.rjust(2,"0")
			time_tuple4 = time_tuple[4]
			time_tuple4 = str(time_tuple4)
			if int(time_tuple4) < 10:
				time_tuple4 = time_tuple4.rjust(2,"0")
			time_tuple5 = time_tuple[5]
			time_tuple5 = str(time_tuple5)
			if int(time_tuple5) < 10:
				time_tuple5 = time_tuple5.rjust(2,"0")
			nd("update",str(time_tuple[0])+time_tuple1+time_tuple2+time_tuple3+time_tuple4+time_tuple5)
			print("版本已更新")
		else:
			print("未知指令，请使用help查看指令")
#判断是否更改文件，如果更改将重复提示异常，否则正常进入
if unlock:
	while unlock != "unlock":
		print("系统异常，错误代码0x000000001")
		time.sleep(3)
yesno = fileok("file","pydos.su\nshutdown.su\nsystem.sys\nload.dll\nprint.dll\nos.dll\nrandom.dll\ntime.dll\ncommand.su\nwordtext.dll\npython.pic")
if yesno == 0:
	while 1:
		print("□□□□□□□□□□□□□□□□□□□□")
		time.sleep(3)
if upsoft:
	start()
else:
	#获取当前时间戳并转换生成到time_tuple列表
	time_tuple = time.localtime(time.time())
	#把列表指定的元素提取并判断是不是两位数，如果是则在左边补0
	time_tuple3 = time_tuple[3]
	time_tuple3 -= 12
	time_tuple3 = str(time_tuple3)
	if int(time_tuple3) < 10:
		time_tuple3 = time_tuple3.rjust(2,"0")
	time_tuple1 = time_tuple[1]
	time_tuple1 = str(time_tuple1)
	if int(time_tuple1) < 10:
		time_tuple1 = time_tuple1.rjust(2,"0")
	time_tuple2 = time_tuple[2]
	time_tuple2 = str(time_tuple2)
	if int(time_tuple2) < 10:
		time_tuple2 = time_tuple2.rjust(2,"0")
	time_tuple4 = time_tuple[4]
	time_tuple4 = str(time_tuple4)
	if int(time_tuple4) < 10:
		time_tuple4 = time_tuple4.rjust(2,"0")
	time_tuple5 = time_tuple[5]
	time_tuple5 = str(time_tuple5)
	if int(time_tuple5) < 10:
		time_tuple5 = time_tuple5.rjust(2,"0")
	nd("update",str(time_tuple[0])+time_tuple1+time_tuple2+time_tuple3+time_tuple4+time_tuple5)
	start()
print("读取更新状态时发生错误")
input("按任意键继续...")