#By sun589(滑稽到滑稽的滑稽)
#安装模块
import base64
import sys
import time
import random
import requests
import re
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="noting here..."#仅为隐藏pygame安装提示,无其他含义
import traceback
from tqdm import tqdm
from pygame import mixer
import socket
import threading
import win32api,win32con
from shutil import  rmtree
############版本号,每次更新请修改!############
version = '2.2'
############版本号,每次更新请修改!############
#更改窗口名称
os.system("title Super Dos")
#关闭requests警告
requests.packages.urllib3.disable_warnings()
#设置pygame_init状态
pygame_init = 0
#切换工作目录
os.chdir(os.path.dirname(sys.executable))
#定义引导函数
def boot(mode:int=0,safemode_fix:int=0):
	"""
	用于引导并初始化
	:param mode: 表示启动模式,0为正常启动,1为safemode,2为oobe
	:param safemode_fix: 表示是否进入修复模式,0为不进入,1为进入
	:return:
	"""
	global oobe_status, rerror, unlock
	os.system('color 07')
	os.system("cls")
	time.sleep(3.6)
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
	global key, opensafe, reg_root, reg_key, reg_flags, reg_path
	if os.path.exists('c:\\superdos_boot.supersystem'):#判断是否被virus破坏
		f = open('c:\\superdos_boot.supersystem')
		if f.read() == '[CRASH]BOOM!':
			while True:
				os.system("cls")
				os.system("color 4F")
				print("""
*****************SuperDos Boot Error!*****************

SuperDos发现boot引导存在错误,请尝试恢复系统或联系厂商!
号码:114-514-1919-18
information:0x000000005
                                   请按Enter以重启...

******************************************************
""")
				input()
				print("Rebooting...")
				time.sleep(2)
				boot()
		f.close()
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
	try:
		oobe_status = win32api.RegQueryValueEx(reg_key,"oobe_status")[0]
	except:
		win32api.RegSetValueEx(reg_key, "oobe_status", 0, win32con.REG_SZ, 'false')
		oobe_status = win32api.RegQueryValueEx(reg_key, "oobe_status")[0]
	try:
		if os.path.isfile("start.bootpic"):
			zi = open("start.bootpic",encoding='utf-8')
			zi = zi.read().split('····')
			print(random.choice(zi))
		else:
			print("nope")
	except PermissionError as e:
		print("字符画文件被占用!",e)
	except:
		print("读取字符画出错!")
	for i in tqdm(range(100),desc='Booting',unit='kb'):
		time.sleep(0.08)
	os.system("cls")
	time.sleep(0.5)
	# 判断是否为第一次使用，是则执行oobe
	if oobe_status != 'true':
		oobe()
	# 判断是否更改值，如果更改将重复提示异常，否则正常进入
	if unlock != "true" and unlock != "false":
		rerror += 1
		raise Exception("unlock status is invaild!")
	if mode == 0:
		while True:
			try:
				start()
			except SystemExit:
				exit(0)
			except KeyboardInterrupt:
				print()
				if input("退出?(y/n)") == 'y':
					exit(0)
				clear()
			except MemoryError:
				memoryerror()
			except:
				# 在这里做个小成就：突破一千行代码:)
				rerror += 1
				error(traceback.format_exc())
	elif mode == 1:
		if safemode_fix == 0:
			while True:
				try:
					safemode(0)
				except SystemExit:
					exit(0)
				except KeyboardInterrupt:
					exit(0)
				except MemoryError:
					memoryerror()
				except:
					rerror += 1
					error(traceback.format_exc())
		else:
			while True:
				try:
					safemode(1)
				except SystemExit:
					exit(0)
				except KeyboardInterrupt:
					exit(0)
				except MemoryError:
					memoryerror()
				except:
					# 在这里做个小成就：突破一千行代码:)
					rerror += 1
					error(traceback.format_exc())
	elif mode == 2:
		while True:
			try:
				oobe()
			except SystemExit:
				exit(0)
			except KeyboardInterrupt:
				exit(0)
			except MemoryError:
				memoryerror()
			except:
				# 在这里做个小成就：突破一千行代码:)
				rerror += 1
				error(traceback.format_exc())
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
                    ------------------------------------
    	''')
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
	print("所有设置已设置完毕，正在重启应用设置！")
	time.sleep(0.75)
	clear()
	boot(0)
rerror = 0#统计错误次数
#定义清屏函数
def clear():
	os.system("cls")
#定义下载文件函数
def download_file(name,url):
	start = time.time()  # 下载开始时间
	headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
	response = requests.get(url, stream=True, headers=headers, verify=False)  # stream=True必须写上
	size = 0  # 初始化已下载大小
	chunk_size = 1024  # 每次下载的数据大小
	content_size = int(response.headers['content-length'])  # 下载文件总大小
	try:
		if response.status_code == 200:  # 判断是否响应成功
			print('[文件大小]:{size:.2f} MB'.format(
				size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
			with open(name, 'wb') as file:  # 显示进度条
				for data in response.iter_content(chunk_size=chunk_size):
					file.write(data)
					size += len(data)
					print('\r' + '[下载进度]:%s%.2f%%' % (
						'>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
		end = time.time()  # 下载结束时间
		print('完成！用时: %.2f秒' % (end - start))  # 输出下载用时时间
	except Exception:
		pass
#定义错误函数
def error(error_message=''):
	global rerror
	global unlock
	global error
	os.system("color 9F")
	clear()
	with open("log.log",'a+') as log:
		log.write(f"[严重错误]\n{error_message}{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n\n")
	clear()
	if rerror == 1:
		print(f'''
.   ((
   (
   (
   (
.   ((
      
当前您的SuperDos可能出了点问题，或许你可以访问bilbili.com/github.com询问作者:)
如需要查询历史错误信息,请在恢复系统后使用check_error指令查询,错误已放置log.log文件
5秒后将会尝试重启来解决...

错误信息:
{error_message}''')
	elif rerror >= 5:
		print("正在进入自动修复模式...")
		boot(1,1)
		rerror = 0
		return
	else:
		print(f'''
.	((
   (  
   (  
   (  
.	((
      
当前您的SuperDos可能出了点问题，或许你可以访问bilbili.com/github.com询问作者:)
如需要查询错误信息,请在恢复系统后使用check_error指令查询,错误已放置log.log文件
检测到这是连续第{rerror}次错误,连续出现五次错误将进入自动修复模式
5秒后将会尝试重启来解决...

错误信息:
{error_message}''')
	time.sleep(5)
	if unlock != 'true' and unlock != 'false':
		rerror += 1
		error()
	clear()
	return
#定义显示内存溢出函数
def memoryerror():
	clear()
	os.system('color 4F')
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
#定义进入安全模式函数
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
	if unlock == 'false':
		win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "false")
	if a == 1:
		print(rerror)
		print("您是否确定修复，如果修复将会锁定system权限！")
		yes = input('(y/n)')
		if yes == 'n':
			if unlock != 'false' and unlock != 'true':
				rerror += 1
				error()
			boot(0)
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
		for i in range(5):
			print("进入修复模式失败:0x000000003")
			print("5秒后即将重试...")
			time.sleep(5)
		raise Exception("0x000000003")
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
		if command == "system_unlock" and unlock == 'false':
			input_key = input("unlockcode:")
			print("校验中...")
			time.sleep(1.2)
			key_str = str(key)
			unlock_key = 0
			for i in key_str:
				unlock_key += ord(i)
			unlock_key *= 1145141919
			unlock_key = base64.b32encode(str(unlock_key).encode('utf-8')).decode('utf-8').replace('=','')
			if input_key == unlock_key:#判断解锁码是否正确，否则提示
				_ = input("解锁将会恢复出厂,你确定吗?(y/n)")
				if _ == 'y':
					print("Unlocking...")
					time.sleep(10)
					win32api.RegSetValueEx(reg_key, "unlock_status", 0, win32con.REG_SZ, "true")
					win32api.RegSetValueEx(reg_key, "oobe_status", 0, win32con.REG_SZ, "false")
					print('Success!')
					time.sleep(0.5)
					print("Rebooting...")
					time.sleep(3)
					clear()
					boot(0)
			else:
				print("校验失败!")
		elif command == "help":
			print('''	system_unlock -- 解锁system
	rebuild -- 修复文件
	reboot -- 重启''')
			if unlock == 'true':
				print('	admin-on -- 打开管理员模式\n	admin-off -- 关闭管理员模式\n	system_lock -- 锁定系统')
		elif command == "reboot":
			time.sleep(2)
			clear()
			boot(0)
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
			boot(0)
		elif command == 'admin-on' and unlock == 'true':
			win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "true")
			print('true')
		elif command == 'admin-off' and unlock == 'true':
			win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "false")
			print('false')
		elif command == 'system_lock' and unlock == 'true':
			if input("锁定将会恢复出厂,你确定吗?(y/n)") == 'y':#判断解锁码是否正确，否则提示
				print("Locking...")
				time.sleep(10)
				win32api.RegSetValueEx(reg_key, "unlock_status", 0, win32con.REG_SZ, "false")
				win32api.RegSetValueEx(reg_key, "oobe_status", 0, win32con.REG_SZ, "false")
				win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "false")
				print("Rebooting...")
				time.sleep(3)
				clear()
				boot(0)
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
	global error_message
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
	print(f"SUPER DOS[版本{version}]\nby bilibili 滑稽到滑稽的滑稽/github sun589")
	while True:#开始循环
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
	update -- 检查更新
	check_error -- 获取错误信息''')
			if unlock == 'true' and admin == 'true':
				print("	admin_write -- 更改程序变量\n	check_work_path -- 获取当前工作目录")
		elif command == "python shell":
			print("Python 3.8.6 Shell")
			print("Input \"exit\" to exit. ")
			while True:
				pycommand = input(">>>")
				if pycommand == 'exit':
					break
				#判断错误
				try:
					exec(pycommand)
				except SyntaxError:
					print("出错了！有可能是因为格式错误(SyntaxError)！")
					print("错误信息：" + traceback.format_exc())
				except TypeError:
					print("发生了类型错误(TypeError)！")
					print("错误信息：" + traceback.format_exc())
				except NameError:
					print('未知命令或者变量错误(NameError)！')
					print("错误信息：" + traceback.format_exc())
				except:
					print("我也不知道发生了什么错误！")
					print("错误信息：" + traceback.format_exc())
		elif command == "python file":
			filename = input('请输入文件名：')
			filename += ".txt"
			try:
				temp = open(filename)
			except:
				print("文件不存在！")
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
			if unlock == "true":#判断解锁状态
				print("当前系统状态:已激活")
				print("当前system解锁状态:Unlock")
				print("序列号:",key)
			elif unlock != "true" and unlock != "false":
				print("出现未知错误！")
				time.sleep(1)
				raise Exception("Something went wrong:(")
			elif unlock == "false":
				print("当前系统状态:已激活")
				print("当前system解锁状态:Locked")
				print("序列号:",key)
			else:
				print("当前系统状态:???")
				print("当前system解锁状态:??????")
				print("序列号:???????????????????????")
		elif command == "reboot safemode":
			print("正在重启...")
			time.sleep(2)
			clear()
			boot(1)
		elif command == "pcg":
			print("正在调用Internet组件并尝试连接网络...")
			time.sleep(3)
			print('''-----------------------------------------------------------
[热门][精华][置顶]SuperDos的unlockcode算法!
评论:
holy [屏蔽],真的吗?
99999999999999999999
太有石粒了吧
system权限,启动!
-----------------------------------------------------------
[帖子]我居然发现了SuperDos解锁system的漏洞！
评论：
哇！谢谢大佬!
有人吗
666666666
大佬nb！
-----------------------------------------------------------
[帖子]SuperDos的权限划分
评论：
看来还是得等yyds大佬搞出install权限（doge）
啥时候才能玩到intsall权限啊（哭）
-----------------------------------------------------------''')
			ok = input("请输入查看帖子的序列号（就是查看第一个输入1这样)(输入其他文字退出)")#让用户确定是否查看
			print("-----------------------------------------------------------")
			if ok == "2":
				print("第一步:进入修复模式\n第二步：输入unlockcode此时就会在系统目录下生成你的解锁码，输入system unlock后输入解锁码就可以解锁了！\n原理大概就是因为官方纯属没有删掉这个指令\n作者：yyds\n日期:2022-09-15")
				print('''-----------------------------------------------------------
2023-12-09更新:unlockcode获取思路没了,官方已经修复了这个漏洞,看来只能我自己去反汇编分析算法了(哭-_-)''')
			elif ok == "3":
				print("SuperDos的权限划分是user<system<install,听说根据zsdn上的yyds大佬分析源代码发现会在系统目录生成各种文件，只有install权限才能查看,不过听说有人获取了install权限并且刷系统成功,说不定以后就会有手机一样的刷机了\n作者：我只是个闲聊的\n日期:2022-08-05")
			elif ok == "1":
				print("是的,我又回来了,时隔2年,这次我发现了unlockcode算法,让我来泄露它吧!\n根据反汇编分析,我发现算法比之前复杂,是将序列号每个字转ascii然后加起来之后乘1145141919之后转[敏感词屏蔽]即为unlockcode\n具体可以使用我做的unlockcode_generate工具\n链接:https://wwap.lanzoum.com/i8sOT1ll248d\n密码:pwd\n输入序列号即可使用\n作者:yyds\n日期:2024-1-19")
			print("-----------------------------------------------------------")
		elif command == "reboot":
			print("正在重启...")
			time.sleep(3)
			clear()
			boot(0)
			break
		elif command == "textmanger":
			filewrite = ''
			name = input("请输入文件：")
			name += ".txt"
			if not os.path.exists('.\\text\\'):
				os.mkdir('text')
			if not os.path.exists(".\\text\\"+name):
				open(".\\text\\"+name,"x").close()
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
			if unlock == "true":#判断是否解锁，下面一样
				win32api.RegSetValueEx(reg_key, "safemode_status", 0, win32con.REG_SZ, "false")
			else:
				print("无权限！")
		elif command == "set safemode 1":
			if unlock == "true":
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
				if unlock == "true":
					print("成功将进程command.su结束，其ID为492")
					while 1:
						input()
				else:
					print("无权限")
			elif taskmgr == "system.sys":
				if unlock == "true":
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
				raise NameError("LOL")
		elif command == "geturl":
			try:
				print("请输入url：")
				url = input()
				print("1.使用get方式请求(默认)\n2.使用post方式请求")
				temp = input()
				if 'https' not in url and 'http' not in url:
					url = 'https://' + url
				if temp == "1":
					data = requests.get(url)
					data.encoding = 'utf-8'
					print("网页状态码："+str(data))
					print("获取内容:\n"+data.text)
				elif temp == "2":
					data = requests.post(url)
					data.encoding = 'utf-8'
					print("网页状态码："+str(data))
					print("获取内容:\n"+data.text)
				else:
					data = requests.get(url)
					data.encoding = 'utf-8'
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
							print(f'网页状态码：{data.status_code}')
							print("获取内容:\n"+data.text)
						elif temp == "2":
							data = requests.post(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200"},verify=False)
							print(f'网页状态码：{data.status_code}')
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
			path = os.path.abspath('.')
			while True:
				clear()
				try:
					list_dir = os.listdir(path)
				except NotADirectoryError:
					print("请输入一个文件夹的名字!")
					path = os.path.abspath(path + '\\..\\')
					list_dir = os.listdir(path)
				except:
					print("读取出错!")
					list_dir = []
				for file_type in list_dir:
					if os.path.isdir(path+"\\"+file_type):
						print(file_type+' '*(32-len(file_type))+'文件夹')
					else:
						print(file_type+' '*(32-len(file_type))+'文件')
				filecommand = input(path+'\\')
				if filecommand == 'close':
					break
				elif filecommand == 'read':
					file = input("file:")
					try:
						if os.path.exists(path+'\\'+file):#判断文件是否存在
							f = open(path+'\\'+file,encoding='utf-8')
							data = f.read()
							f.close()
							print("-------------data-------------")
							print(data)
							print("-------------data-------------")
						else:
							print("文件不存在")
					except UnicodeDecodeError:
						print("请检查文件编码是否为utf-8!")
					except Exception as e:
						print("读取文件时发生错误，请检查格式是否适合读取或者是否存在！")
						print(e)
					input()
					clear()
				elif filecommand == 'del':
					file = input("file:")
					if os.path.exists(path+'\\'+file):
						if os.path.isfile(path+'\\'+file):
							os.remove(path+'\\'+file)
						else:
							rmtree(path+'\\'+file)
					else:
						print("文件不存在")
					print("删除完成!")
					input()
					clear()
				elif filecommand == 'rename':
					name = input("file:")
					name_new = input("newname:")
					if os.path.exists(path+'\\'+name):
						os.rename(path+'\\'+name,name_new)
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
					path = os.path.abspath('.')
					continue
				elif filecommand == "copy":
					file = input("file:")
					if os.path.exists(path+'\\'+file):
						temp = open(path+'\\'+file,'rb')
						data = temp.read()
						temp.close()
						status = "1"
						print("ok")
						input()
					else:
						print("文件不存在")
				elif filecommand == "paste":
					if status == "1":
						f = open(path+'\\'+file,'wb')
						f.write(data)
						print("ok")
						input()
					else:
						print("剪切板无内容")
						input()
				elif filecommand == 'nd':
					try:
						os.mkdir(path+'\\'+input("请输入文件夹:"))
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
					input()
				elif filecommand == 'up':
					path = os.path.abspath(path+'\\..\\')
				else:
					if os.path.exists(path+'\\'+filecommand):
						path = os.path.abspath(path+'\\'+filecommand)
				clear()
		elif command == "chinese":
			try:
				json = {'kw':input("翻译内容：")}
				url = "https://fanyi.baidu.com/sug"
				data = requests.post(url,data=json,timeout=8)
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
			while True:
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
				f = open(r"c:\superdos_boot.supersystem",'w')
				f.write("[CRASH]BOOM!")
				f.close()
				pf = open(r"c:\password.txt",'w')
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
				while True:
					if c == 3:
						print("看来你是真不知道密码，不过根据规定，我还是得把你的系统搞崩溃:)")
						time.sleep(5)
						clear()
						print("由于发现部分内存区异常，Super Dos正在扫描异常内存以方便修复!")
						time.sleep(3)
						for x in range(1000000,1200000):
							print("0x"+str(x).rjust(7,'0')+" error!")
						clear()
						for i in range(500):
							print(random.choice(['螟', 'ｧ', '螳', 'ｶ', '螂', 'ｽ', '謌', '第', '弍', '隸', 'ｴ', '逧', '�', '％', '逅', '�', 'ｦ', 'よ', '擂', '莉', '紋', 'ｺ', '�', '雛', '蝠', 'ｦ', '霎', '｣', '闔', 'ｫ', '髞', '滓', '巳', '諡', 'ｷ', '辜', 'ｫ', '蜊', 'ｧ', '讒', 'ｽ']),end='')
							time.sleep(0.05)
						raise SystemError("BOOM!")
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
			while True:
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
				except:
					continue
			print("播放结束")
		elif command == 'download':
			url = input("请输入网址：")
			download_name = input("名称：")
			if url:
				download_file(download_name,url)
		elif command == 'oobe':
			if input("y/n?") == 'y:':
				time.sleep(2)
				oobe()
		elif command == 'superchat':
			change = input("1.创建房间\n2.加入房间\n")
			if change == '1':
				try:
					server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
					server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
					port = random.randint(2333,10000)
					hostname = socket.gethostname()
					ip_address = socket.gethostbyname(hostname)
					server.bind((ip_address,port))
					print(f"服务器已向{ip_address}:{port}发起连接(仅同个网络下的电脑可连接)(ctrl+c退出)...")
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
				except KeyboardInterrupt:
					pass
			elif change == '2':
				try:
					ip = input("输入ip:")
					port = int(input("输入端口:"))
					print("connecting...")
					client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
		elif command == 'admin-write' and unlock == 'true' and admin == 'true':
			change = input('注意！前方为开发者区域，随意修改很可能导致崩溃！！！(y/n):')
			if change=='y':
				print('输入exit退出')
				for name, value in globals().copy().items():
					print(f'{name}={value}\ttype={type(value)}')
				write_name = input('请输入更改的变量名:')
				write_text = input('输入更改的文字:')
				while True:
					write_type = input("输入值的类型(int,list,string,float,bool):")
					try:
						if write_type == 'int':
							write_text = int(write_text)
						elif write_type == 'list':
							write_text = list(write_text)
						elif write_type == 'string':
							pass
						elif write_type == 'float':
							write_text = float(write_text)
						elif write_type == 'bool':
							write_text = float(write_text)
						else:
							print("非支持的类型")
							continue
					except:
						print("出错!")
					break
				globals()[write_name] = write_text
				print('done!')
		elif command == 'update':
			try:
				print("正在获取更新...")
				api = "https://api.github.com/repos/sun589/Super-Dos/releases/latest"#设置api
				try:
					update = requests.get(api,verify=False,timeout=10)#爬取github上的更新时间
					update_message = update.json()#转换为json字典
					print(f"最新版本:{update_message['name'][-3:]} 当前版本:{version}")
					if update_message['name'][-3:] > version:#检测当前更新版本是否低于github上的版本，如果高于说明有更新
						print(f"检测到新版本:{update_message['html_url'][-3:]}")
						print(f"更新信息:{update_message['body']}")
						yes = input("是否更新?(Yes/No):")
						if yes == "Y" or yes == 'y' or yes == 'Yes' or yes == 'yes':
							print("正在下载中....")
							download_file('new_os.exe',update_message['assets'][0]['browser_download_url'])
							print("下载完毕!请使用new_os.exe开机来使用新系统!")
					else:
						print("暂无新系统！")
				except:
					print("出错!")
			except:
				print("获取更新时出现了未知错误！")
		elif command == 'check_error':
			if os.path.isfile('log.log'):
				error_messages = open('log.log').read().split('\n\n')
				del error_messages[-1]
				if len(error_messages) <= 0:
					print("暂无错误信息!")
				else:
					print(f"你总共有{len(error_messages)}条错误,请输入需要获取的信息(从久远到最新,如需要最新的错误信息输入-1;如需获取全部输入-2)")
					try:
						a = int(input())
						if a == -1:
							print(error_messages[-1])
						elif a == -2:
							print('\n\n'.join(error_messages))
						else:
							print(error_messages[a-1])
					except:
						print("请输入有效的序号!")
			else:
				print("暂无错误信息!")
		elif command == 'check_work_path' and admin == 'true':
			print(os.getcwd())
		else:
			print("未知命令，请用help查看")
		rerror = 0
if __name__ == '__main__':
	boot(mode=0)