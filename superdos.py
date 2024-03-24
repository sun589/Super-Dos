# By sun589(滑稽到滑稽的滑稽)
# 安装模块
import base64
import shutil
import sys
import time
import random
import requests
import re
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "noting here..."  # 仅为隐藏pygame安装提示,无其他含义
import traceback
from tqdm import tqdm
from tqdm.rich import tqdm as tqdm_rich
from pygame import mixer
import socket
import threading
import win32api, win32con
from shutil import rmtree
from warnings import simplefilter
from rich.table import Table
from rich.console import Console
from json import loads
from rich.syntax import Syntax
############版本号,每次更新请修改!############
version = '2.6'
############版本号,每次更新请修改!############
debug = False
# 更改窗口名称
os.system("title SuperDos")
# 关闭警告
requests.packages.urllib3.disable_warnings()
simplefilter("ignore")
# 设置pygame_init状态
pygame_init = 0
# 功能列表,用于补全指令
functions = ['shutdown', 'textmanger', 'python shell', 'python file', 'info', 'reboot', 'reboot safemode', 'title',
             'taskmgr', 'errortest',
             'geturl', 'filemanger', 'chinese', 'music', 'superchat', 'update', 'paint',
             'calc','check_error','help','start','software shop','python shell','python file']
rerror = 0  # 统计错误次数
# 切换工作目录
if os.path.basename(sys.executable) != 'python.exe':
    os.chdir(os.path.dirname(sys.executable))
# 定义引导函数
def boot(mode: int = 0, safemode_fix: int = 0):
    """
	用于引导并初始化
	:param mode: 表示启动模式,0为正常启动,1为safemode,2为oobe,3为recovery
	:param safemode_fix: 表示是否进入修复模式,0为不进入,1为进入
	"""
    boot_flag = False
    s = 'FAILED TO BOOT!'
    try:
        global oobe_status, rerror, unlock, n, key, opensafe, reg_root, reg_key, reg_flags, reg_path, admin
        os.system('color 07')
        os.system("cls")
        time.sleep(3.6)
        if os.path.exists('c:\\superdos_boot.supersystem'):  # 判断是否被virus破坏
            f = open('c:\\superdos_boot.supersystem')
            if f.read() == '[CRASH]BOOM!':
                print("\r328KB Bad!", end='', flush=True)
                time.sleep(3)
                print("\r625KB Bad!", end='', flush=True)
                time.sleep(1)
                print("\r1024KB Bad!", end='', flush=True)
            else:
                print("\r328KB OK", end='', flush=True)
                time.sleep(3)
                print("\r625KB OK", end='', flush=True)
                time.sleep(1)
                print("\r1024KB OK", end='', flush=True)
            f.close()
        else:
            print("\r328KB OK", end='', flush=True)
            time.sleep(3)
            print("\r625KB OK", end='', flush=True)
            time.sleep(1)
            print("\r1024KB OK", end='', flush=True)
        time.sleep(0.5)
        print("\rcpu:antel s9 10002K", end='', flush=True)
        time.sleep(0.5)
        print("\rgpu:stx 4090ti       ", end='', flush=True)
        time.sleep(0.5)
        print("\rram:1024KB         ", end='', flush=True)
        time.sleep(1)
        clear()
        time.sleep(1)
        # 设置操作注册表的各种东西
        reg_root = win32con.HKEY_CURRENT_USER
        reg_path = "SOFTWARE\\Superdos"
        reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS
        win32api.RegCreateKeyEx(reg_root, reg_path, reg_flags)
        reg_key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
        if mode == 3:
            recovery()
            sys.exit(0)
        if os.path.exists('c:\\superdos_boot.supersystem'):  # 判断是否被virus破坏
            with open("c:\\superdos_boot.supersystem") as f:
                boot_text = f.read()
                if boot_text == '[CRASH]YOUR_PC_IS_LOCK_NOW':
                    lock()
                    sys.exit()
                if boot_text == "[CRASH]BOOM!":
                    boot_error('FAILED TO BOOT!')
        # 读取序列号
        try:
            key = win32api.RegQueryValueEx(reg_key, "system_key")[0]
        except:  # 判断序列号是否存在，不存在创建
            win32api.RegSetValueEx(reg_key, "system_key", 0, win32con.REG_SZ,str(random.randint(10000000000000, 99999999999999)))
            key = win32api.RegQueryValueEx(reg_key, "system_key")[0]
        # 读取安全模式是否可以进入
        try:
            opensafe = win32api.RegQueryValueEx(reg_key, "safemode_status")[0]
        except:
            win32api.RegSetValueEx(reg_key, "safemode_status", 0, win32con.REG_SZ, 'true')
            opensafe = win32api.RegQueryValueEx(reg_key, "safemode_status")[0]
        # 读取解锁状态
        try:
            unlock = win32api.RegQueryValueEx(reg_key, "unlock_status")[0]
        except:
            win32api.RegSetValueEx(reg_key, "unlock_status", 0, win32con.REG_SZ, 'false')
            unlock = win32api.RegQueryValueEx(reg_key, "unlock_status")[0]
        try:
            oobe_status = win32api.RegQueryValueEx(reg_key, "oobe_status")[0]
        except:
            win32api.RegSetValueEx(reg_key, "oobe_status", 0, win32con.REG_SZ, 'false')
            oobe_status = win32api.RegQueryValueEx(reg_key, "oobe_status")[0]
        try:
            admin = win32api.RegQueryValueEx(reg_key, "admin_status")[0]
        except:
            win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, 'false')
            admin = win32api.RegQueryValueEx(reg_key, "admin_status")[0]
        try:
            if os.path.isfile("start.bootpic"):
                zi = open("start.bootpic", encoding='utf-8')
                zi = zi.read().split('····')
                print(random.choice(zi))
            else:
                print("nope")
        except PermissionError as e:
            print("字符画文件被占用!", e)
        except:
            print("读取字符画出错!")
        if os.path.isfile('c:\superdos_boot.supersystem'):
            n = random.randint(11,100)  # 用于生成是否显示virus和彩蛋
        else:
            n = random.randint(0, 100)
        if n == 66 and os.path.isfile('c:\superdos_boot.supersystem'):
            n = 11
        if debug != True:
            if n >= 95:
                print("恭喜解锁彩蛋:进度条似乎有点不一样?")
                process = tqdm_rich(range(100), desc='Booting', unit='kb')
            else:
                process = tqdm(range(100), desc='Booting', unit='kb')
            for i in process:
                if n <= 10 or n == 66:
                    time.sleep(0.2)
                else:
                    time.sleep(0.08)
        clear()
        if n <= 10 and oobe_status == 'true':
            print("\r检测到外来未知IP地址??.??.??.???进入,请立即关机!",end='',flush=True)
            time.sleep(0.7)
            os.system('color 4F')
            print('\r潤瑣灹⁥瑨汭㰾瑨汭㰾敨摡㰾敭慴挠慨獲瑥瑵㘱㸢琼瑩敬唾瑮',flush=True)
        time.sleep(0.3)
        os.system('color 07')
        clear()
        # 判断是否为第一次使用，是则执行oobe
        if oobe_status == 'false':
            oobe()
        if len(str(key)) != 14:
            boot_error("Serial number is invaild!")
        for i in str(key):
            if not ('0' <= i <= '9'):
                boot_error("Serial number is invaild!")
        if oobe_status == 'false' and oobe_status != 'true':
            boot_error("oobe status is invaild!")
        # 判断是否更改值，如果更改将重复提示异常，否则正常进入
        if unlock != "true" and unlock != "false":
            rerror += 1
            boot_error("unlock status is invaild!")
    except Exception as e:
        boot_flag = True
        s = repr(e)
    if boot_flag == True:
        boot_error(s)
    while True:
        r_flag = False
        errmessage = ''
        try:
            if mode == 0:
                start()
            elif mode == 1:
                if safemode_fix == 1:
                    safemode(1)
                else:
                    safemode()
            elif mode == 2:
                oobe()
            elif mode == 3:
                recovery()
            elif mode == -2:
                clear()
                print("Super Anti-virus正在安装Ruvis-WaHjkP补丁...")
                with open("c:\\superdos_boot.supersystem",'w') as f:
                    f.write('')
                time.sleep(3)
                print("安装成功,正在重启...")
                time.sleep(1)
                boot(0)
            else:
                print("恭喜解锁彩蛋:Where should I go???")
                break
        except SystemExit:
            sys.exit(0)
        except KeyboardInterrupt:
            sys.exit(0)
        except MemoryError:
            memoryerror()
        except:
            if mode == 3:
                print("Something went error!")
            else:
                rerror += 1
                r_flag = True
                errmessage = traceback.format_exc()
        if r_flag == True:
            error(errmessage)
def oobe():
    """
    开箱体验模式,用于首次使用设置
    """
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
    win32api.RegSetValueEx(reg_key, "color", 0, win32con.REG_SZ, color + colorfont)
    os.system("cls")
    win32api.RegSetValueEx(reg_key, "oobe_status", 0, win32con.REG_SZ, 'true')
    print("所有设置已设置完毕，正在重启应用设置！")
    time.sleep(1)
    clear()
    boot(0)
# 定义清屏函数
def clear():
    os.system("cls")
def lock():
    try:
        while True:
            clear()
            os.system('color fc')
            print("""
                  ,]@@@@@@@@@@@@\`                   
               ,O@@@@@@@@@@@@@@@@@@@`                
              @@@@@@@@@@@@@@@@@@@@@@@@`              
            =@@@@@@@@@@@@@@@@@@@@@@@@@@\             
           =@@@@`     ,@@@@@@^      @@@@\            
           @@@@@       @@@@@@`      /@@@@^           
          =@@@@@@`    /@@/\@@@`    /@@@@@@           
          =@@@@@@@@@@@@@^  ,@@@@@@@@@@@@@@           
          =@@@@@@@@@@@@^     @@@@@@@@@@@@^           
           ,\@@@@@@@@@@@@@@@@@@@@@@@@@@@`            
                =@@@@@@@@@@@@@@@@@@^                 
       ]@@@`    =@@@@@@@@@@@@@@@@@@^    ,/@@\        
      @@@@@@O   =@@@@@@@@@@@@@@@@@@^   =@@@@@@`      
      @@@@@@/    ,@@@@@@@@@@@@@@@@[    =@@@@@@`      
    ,@@@@@@@@@]`                     ]@@@@@@@@@\     
   =@@@@@@@@@@@@@@\]            ,/@@@@@@@@@@@@@@\    
   ,@@@@@@`,[@@@@@@@@@@\`   ]@@@@@@@@@@/` O@@@@@^    
     ,[[`       [\@@@@@@@@@@@@@@@@@[        [[[      
                  ,/@@@@@@@@@@@@\`                   
    ,@@@@`    ]@@@@@@@@@@O\@@@@@@@@@@]`   ,@@@@\     
   =@@@@@@@@@@@@@@@@@[`       [@@@@@@@@@@O@@@@@@\    
   ,@@@@@@@@@@@@/`                ,\@@@@@@@@@@@@^    
     ,\@@@@@/                          [@@@@@@`      
      @@@@@@@                          =@@@@@@^      
      =@@@@@`                          ,@@@@@/       
                                                     
OOPS!
你需要密码才能启动!
看起来你被我攻击了,但是你很幸运,你只需支付114514元到我的账户上就行,就给你密码
My_PayBaby_Account:JgYTkbYJoUbHg_191900.onion@pay
你只需打开PayBaby就能支付|https://jee.li/paybaby
没钱?没关系,玩点智力解,我把密码放在了Github上,或许你可以去那找找密码""")
            if input("Password:") == 'im_a_pupil_unlock_my_pc_plz':
                print("密码正确!")
                time.sleep(0.8)
                print("解锁中...")
                with open("c:\\superdos_boot.supersystem",'w') as f:
                    f.write('')
                time.sleep(3)
                print("解锁成功,按下回车后重启")
                input()
                boot(0)
    except Exception as e:
        print(e)
# 定义下载文件函数
def download_file(name, url):
    start = time.time()  # 下载开始时间
    html_down = False
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
    try:
        response = requests.get(url, stream=True, headers=headers, verify=False)# stream=True必须写上
    except:
        print("获取数据时出错!")
        return
    size = 0  # 初始化已下载大小
    chunk_size = 1024  # 每次下载的数据大小
    try:
        content_size = int(response.headers['content-length'])  # 下载文件总大小
    except:
        html_down = True
    try:
        if response.status_code == 200:  # 判断是否响应成功
            if html_down == True:
                with open(name,'wb') as f:
                    j = 0
                    for i in response.iter_content(chunk_size=512):
                        f.write(i)
                        j += 0.2
                        print(f'\r[下载进度]:{">"*int(j)}',end='',flush=True)
                for i in range(10-j):
                    print(">",end='',flush=True)
                print()
            else:
                print('[文件大小]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
                with open(name, 'wb') as file:  # 显示进度条
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        print('\r' + '[下载进度]:%s%.2f%%' % (
                            '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ', flush=True)
        end = time.time()  # 下载结束时间
        print('完成！用时: %.2f秒' % (end - start))  # 输出下载用时时间
    except Exception as e:
        print()

# 定义引导错误函数
def boot_error(error_message='NULL'):
    """
    引导报错模式,用于处理报错
    :param error_message: 错误信息
    """
    os.system("cls")
    os.system("color 4F")
    n = '\n'#为了在f-string里使用\n
    print(f"""
*****************SuperDos Boot Error!*****************

SuperDos在进行引导时发生错误,请尝试恢复系统或联系厂商!
号码:114-514-191-918
ERROR CODE:0x000000005
Information:{error_message}
{"根据分析错误疑似为系统代码层级错误,请联系作者!" if 'Error' in error_message else '您可尝试访问 https://sun589.github.io/wiki/errcode 以寻求帮助'}

                                 请按Enter以重启...

******************************************************
	""")
    input()
    print("Rebooting...")
    time.sleep(2)
    boot(0)
# 定义错误函数
def error(error_message='NULL'):
    """
    日常使用报错模式(BSOD),用于处理报错
    :param error_message:
    :return:
    """
    global rerror
    global unlock
    global error
    os.system("color 9F")
    clear()
    try:
        with open("log.log", 'a+') as log:
            log.write(f"[严重错误]\n{error_message}{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n\n")
    except PermissionError:
        print("日志写入失败,请检查程序执行目录是否在c盘或者检查日志文件是否关闭被占用!")
    except Exception as e:
        print(f"日志写入失败,原因:{repr(e)}")
    clear()
    if rerror == 1:
        print(f'''
.   ((
   (
   (
   (
.   ((
      
当前您的SuperDos可能出了点问题，或许你可以访问bilbili.com/github.com询问作者:)
如需要查询历史错误信息,请在系统恢复后使用check_error指令查询,错误已放置log.log文件
5秒后将会尝试重启来解决...

错误信息:
{error_message}''')
    elif rerror >= 5:
        print("正在进入自动修复模式...")
        boot(1, 1)
        rerror = 0
        boot(0)
    else:
        print(f'''
.	((
   (  
   (  
   (  
.	((
      
当前您的SuperDos可能出了点问题，或许你可以访问bilbili.com/github.com询问作者:)
如需要查询错误信息,请在系统恢复后使用check_error指令查询,错误已放置log.log文件
检测到这是连续第{rerror}次错误,连续出现五次错误将进入自动修复模式
5秒后将会尝试重启来解决...

错误信息:
{error_message}''')
    time.sleep(5)
    if unlock != 'true' and unlock != 'false':
        rerror += 1
        error()
    clear()
    if 'Super Anti-virus 已拦截!' in error_message:
        boot(-2)
    else:
        boot(0)
# 定义显示内存溢出函数
def memoryerror():
    """
    内存溢出处理
    """
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
# 定义进入恢复模式函数
def recovery():
    """
    Recovery模式,用于修复底层数据
    """
    os.system('color 17')
    for i in range(6):
        print(f"\rLoading fix.su {'.' * i}", end='', flush=True)
        time.sleep(2)
    os.system('cls')
    print("欢迎进入Recovery模式!")
    while True:
        command = input('Recovery>')
        if command == 'help':
            print("""	help -- 帮助
	fix_all -- 修复全部(包括底层,将清除一切)
	fix -- 修复部分(可解决80%问题,可保留数据)
	reset_system -- 恢复出厂设置
	reboot -- 重启
	all_reboot_mode -- 高级重启""")
        elif command == 'fix_all':
            if input("这将会重置你的SN码,你确定吗?(y/n)") == 'y':
                print("fixing..")
                reg_parent, subkey_name = os.path.split(reg_path)
                r_key = win32api.RegOpenKeyEx(reg_root, reg_parent, 0, reg_flags)
                win32api.RegDeleteKeyEx(r_key, subkey_name)
                with open("c:\\superdos_boot.supersystem", 'w') as f:
                    f.write('')
                if os.path.isdir('Program'):
                    shutil.rmtree('Program')
                time.sleep(8)
                print("fixed!")
        elif command == 'fix':
            print("即将跳转至修复模式...")
            time.sleep(3)
            os.system('cls')
            print("您是否确定修复，如果修复将会锁定system权限！")
            yes = input('(y/n)')
            if yes =='y':
                print("开始修复...")
                win32api.RegSetValueEx(reg_key, "unlock_status", 0, win32con.REG_SZ, "false")
                win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "false")
                time.sleep(0.5)
                print("修复完成！")
        elif command == 'reboot':
            boot(mode=0)
        elif command == 'all_reboot_mode':
            print("""0.正常启动
1.以safemode模式启动
2.以oobe模式启动
3.以recovery模式启动""")
            try:
                reboot_mode = int(input())
                boot(mode=reboot_mode)
            except:
                print("FAILED!")
        elif command == 'reset_system':
            if input("确定?(y/n):") == 'y':
                win32api.RegSetValueEx(reg_key, "oobe_status", 0, win32con.REG_SZ, "false")
                if os.path.isdir('Program'):
                    shutil.rmtree('Program')
                time.sleep(5)
                boot(mode=0)
        elif command == '':
            pass
        else:
            print("未知指令,请用help查看指令")
# 定义进入安全模式函数
def safemode(a=0):
    """
    SafeMode模式,用于修复系统
    :param a: 是否进入修复模式 0为否 1为是
    """
    global unlock
    global rerror
    global admin
    if unlock == 'false':
        try:
            admin = win32api.RegQueryValueEx(reg_key, "admin_status")[0]
        except:
            win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, 'false')
            admin = win32api.RegQueryValueEx(reg_key, "admin_status")[0]
    if a == 1:
        print("您是否确定修复，如果修复将会锁定system权限！")
        yes = input('(y/n)')
        if yes == 'n':
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
    # 将全局变量带入局部变量
    global key
    opensafe = win32api.RegQueryValueEx(reg_key, 'safemode_status')[0]
    if opensafe == 'false':
        for i in range(5):
            print("进入修复模式失败:0x000000003")
            print("5秒后即将重试...")
            time.sleep(5)
        raise Exception("0x000000003")
    print("Loading system....")
    time.sleep(3)
    print("Loading safemode.dll...")
    time.sleep(5)
    print('''Loading command.su
	Loading drives.sys
	Loading drivesystem.sys''')
    time.sleep(1)
    clear()
    password = win32api.RegQueryValueEx(reg_key, 'password')[0]
    if password:
        for _ in range(3):
            if input("请输入密码(超过三次自动关机):") == password:
                break
            else:
                print("密码错误！")
        else:
            sys.exit()
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
            unlock_key = base64.b32encode(str(unlock_key).encode('utf-8')).decode('utf-8').replace('=', '')
            if input_key == unlock_key:  # 判断解锁码是否正确，否则提示
                _ = input("解锁将会恢复出厂,你确定吗?(y/n)")
                if _ == 'y':
                    print("Unlocking...")
                    time.sleep(10)
                    win32api.RegSetValueEx(reg_key, "unlock_status", 0, win32con.REG_SZ, "true")
                    win32api.RegSetValueEx(reg_key, "oobe_status", 0, win32con.REG_SZ, "false")
                    if os.path.isdir('Program'):
                        shutil.rmtree('Program')
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
                print('	admin_on -- 打开管理员模式\n	admin_off -- 关闭管理员模式\n	system_lock -- 锁定系统')
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
            if input("锁定将会恢复出厂,你确定吗?(y/n)") == 'y':  # 判断解锁码是否正确，否则提示
                print("Locking...")
                time.sleep(10)
                win32api.RegSetValueEx(reg_key, "unlock_status", 0, win32con.REG_SZ, "false")
                win32api.RegSetValueEx(reg_key, "oobe_status", 0, win32con.REG_SZ, "false")
                win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "false")
                if os.path.isdir('Program'):
                    shutil.rmtree('Program')
                print("Rebooting...")
                time.sleep(3)
                clear()
                boot(0)
        else:
            print("未知命令，请用help查看")

def start():
    """
    NormalMode模式,用于日常使用
    """
    password = win32api.RegQueryValueEx(reg_key, 'password')[0]
    if password:
        for _ in range(3):
            if input("请输入密码(超过三次自动关机):") == password:
                clear()
                break
            else:
                print("密码错误！")
        else:
            sys.exit()
    global unlock
    global rerror
    global admin
    if admin == 'true' and unlock == 'false':
        win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "false")
    os.system(f"color {win32api.RegQueryValueEx(reg_key, 'color')[0]}")
    global key  # 把key变量带入局部变量
    global pygame_init
    global error_message
    global n
    # 读取解锁状态，防止解锁后无法检测到
    unlock = win32api.RegQueryValueEx(reg_key, 'unlock_status')[0]
    # 读取admin状态，原因同上
    admin = win32api.RegQueryValueEx(reg_key, "admin_status")[0]
    # 读取用户名
    user_name = win32api.RegQueryValueEx(reg_key, 'Name')[0]
    print(f"SUPER DOS[版本{version}]{'[Debug]' if debug == True else ''}\nby bilibili 滑稽到滑稽的滑稽/github sun589")
    while True:  # 开始循环
        command = input(f"{user_name}>")  # 输入命令
        rerror = 0
        # 判断命令并执行相对应的指令
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
            sys.exit()
        elif command == "help":
            print('''	help -- 帮助
	shutdown -- 关机
	textmanger -- 文件助手
	python shell -- 进入python shell 3.8.6
	python file -- 用python执行文件（可用文本助手/Python IDE创建）
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
	music -- 音乐播放器
	superchat -- 聊天
	update -- 检查更新
	check_error -- 获取错误信息
	software shop -- 软件商店
	start -- 运行软件''')
            if admin == 'true':
                print("	admin_write -- 更改程序变量\n	check_work_path -- 获取当前工作目录\n	all_system_info -- 查看系统所有信息")
            if n <= 10:
                print("	virus -- A present for you:)")
        elif command == "python shell":
            clear()
            print("Python 3.8.6 Shell")
            print("Input \"exit\" to exit. ")
            local_vars = {}
            while True:
                pycommands = []
                pycommand = input(">>> ")
                if pycommand == '':
                    continue
                if pycommand == 'exit':
                    break
                pycommands.append(pycommand)
                if pycommand[-1] == ':':
                    while True:
                        pycommand_c = input('....')
                        if pycommand_c == '':
                            break
                        pycommands.append(pycommand_c)
                        continue
                flag = False # 判断是否触发NoneType
                # 判断错误
                try:
                    exec('\n'.join(pycommands),local_vars)
                except SyntaxError as e:
                    print("出错了！有可能是因为格式错误(SyntaxError)！")
                    print(f"错误信息:{repr(e)}")
                except TypeError as e:
                    print("发生了类型错误(TypeError)！")
                    print(f"错误信息:{repr(e)}")
                except NameError as e:
                    print('未知命令或者变量错误(NameError)！')
                    print(f"错误信息:{repr(e)}")
                except KeyboardInterrupt:
                    print('手动退出(KeyboardInterrupt)！')
                except ZeroDivisionError as e:
                    print("0不能作为除数啊!!!!")
                    print(f"错误信息:{repr(e)}")
                except Exception as e:
                    print("我也不知道发生了什么错误!")
                    print(f"错误信息:{repr(e)}")
                else:
                    continue
            del local_vars
            clear()
        elif command == "python file":
            filename = input('请输入文件名(在py目录下请在前面加.\\py\\)：')
            try:
                temp = open(filename, encoding='utf-8')
                pycommandfile = temp.read()
                temp.close()
            except FileNotFoundError:
                print("文件不存在!")
            except Exception as e:
                print("报错！")
                print(e)
            else:
                print("提示:如需退出请按下Ctrl+C随时退出")
                print("-----------程序已开始-----------")
                try:
                    exec(pycommandfile)
                except SyntaxError as e:
                    print("出错了！有可能是因为格式错误(SyntaxError)！")
                    print(f"错误信息:{repr(e)}")
                except TypeError as e:
                    print("发生了类型错误(TypeError)！")
                    print(f"错误信息:{repr(e)}")
                except NameError as e:
                    print('未知命令或者变量错误(NameError)！')
                    print(f"错误信息:{repr(e)}")
                except KeyboardInterrupt:
                    print('手动退出(KeyboardInterrupt)！')
                except ZeroDivisionError as e:
                    print("0不能作为除数啊!!!!")
                    print(f"错误信息:{repr(e)}")
                except Exception as e:
                    print("我也不知道发生了什么错误!")
                    print(f"错误信息:{repr(e)}")
                print("-----------程序已结束-----------")
        elif command == "info":
            # 利用布尔值判断序列号是否为空，如果为空则生成
            if unlock == "true":  # 判断解锁状态
                print("当前系统状态:已激活")
                print("当前system解锁状态:Unlocked")
                print("序列号:", key)
            elif unlock == "false":
                print("当前系统状态:已激活")
                print("当前system解锁状态:Locked")
                print("序列号:", key)
            elif unlock != "true" and unlock != "false":
                print("出现未知错误！")
                time.sleep(1)
                raise Exception("Something went wrong:(")
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
            print("正在调用Internet组件并尝试连接网络...",end='',flush=True)
            time.sleep(3)
            if n == 66:
                for i in range(200):
                    print(random.choice([1,0]),end='',flush=True)
                    time.sleep(0.00001)
                clear()
                time.sleep(3)
                with open("c:\\superdos_boot.supersystem", 'w') as f:
                    f.write('[CRASH]YOUR_PC_IS_LOCK_NOW')
                print("[Warning] @ Connection_from_98.25.00.138")
                time.sleep(1)
                print(f"[WebServer] Opened Internet server on {socket.gethostbyname(socket.gethostname())}:7070")
                time.sleep(5)
                print("[Internet server] Received requests from 98.25.00.138")
                time.sleep(3)
                print("""
Traceback(most recent call last):
 Function<Super_Internet_module>, line 211, in <decode_module>
  decode_message(string,"utf-8")
UnknownError:Decode text failed!""")
                time.sleep(4)
                print("Injecting virus...")
                for i in range(7):
                    print(".", end='', flush=True)
                    time.sleep(1)
                print()
                os.system('color 4f')
                time.sleep(0.8)
                sys.exit(0)
            else:
                print()
            if n <= 10:
                print("""-----------------------------------------------------------
[???]增强系统性能和功能教程!
评论:
非常有用,谢谢!
9999999999999999999
超级大佬,谢谢!
-----------------------------------------------------------""")
            else:
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
-----------------------------------------------------------
[帖子][精华]被virus感染后如何抢救
评论:
感谢!成功救回!
谢谢!
nb!
-----------------------------------------------------------
[帖子]一个献给所有大佬的软件!
评论:
为啥提示非法程序啊?
假的假的,散了吧
一群sz不会用就说假的,要是门槛拉这么低谁都能用的话出问题不得被骂死?
可以啊大神
-----------------------------------------------------------''')
            ok = input("请输入查看帖子的序列号(就是查看第一个输入1这样)(输入其他文字退出):")  # 让用户确定是否查看
            print("-----------------------------------------------------------")
            if n <= 10:
                print("退出到终端,输入virus并且回车,and enjoy my present for you:)\n作者:????\n日期:????-??-??")
            elif ok == "1":
                print("是的,我又回来了,时隔2年,这次我发现了unlockcode算法\n根据反汇编分析,我发现算法比之前复杂,是将序列号每个字转ascii然后加起来之后乘1145141919之后转[敏感词屏蔽]即为unlockcode\n具体可以使用我做的unlockcode_generate工具\n链接:https://wwap.lanzoum.com/i8sOT1ll248d\n密码:pwd\n输入序列号即可使用\n作者:yyds\n日期:2024-1-19")
            elif ok == "2":
                print("第一步:进入修复模式\n第二步：输入unlockcode此时就会在系统目录下生成你的解锁码，输入system unlock后输入解锁码就可以解锁了！\n原理大概就是因为官方纯属没有删掉这个指令\n作者：yyds\n日期:2022-09-15")
                print('''-----------------------------------------------------------
2023-12-09更新:unlockcode获取思路没了,官方已经修复了这个漏洞,看来只能我自己去反汇编分析算法了(哭-_-)''')
            elif ok == "3":
                print("SuperDos的权限划分是user<system<admin,听说根据zsdn上的yyds大佬分析源代码发现会在系统目录生成各种\"键\"，只有admin权限才能查看,不过听说有人获取了admin权限并且刷系统成功,说不定以后就会有手机一样的刷机了\n作者：我只是个闲聊的人\n日期:2022-08-05")
            elif ok == '4':
                print("最近,一款名为virus的新型病毒急速扩散,大部分用户已中招,\n目前官方已经有了解决方法(听说本论坛有hacker入侵诱导用户执行virus,每一位的电脑都被植入了,但因权限无法自动执行),\n目前可以通过\"superdos.exe 3\"指令启动superdos并进入recovery,此时务必输入fix_all以修复\n(注:请勿输入fix,这并不会修复系统,因为此病毒深入到了底层结构!)\n作者:yyds\n日期:2024-1-29")
            elif ok == '5':
                print("最近做了款软件,叫\"KingTools\",这款软件是为各位大佬和破解者研究用的,在software shop即可下载\n这里面包含了我所有的破解知识,里面有着获取解锁码/暴击解锁/开启debug等功能\n不过使用也是有门槛的,如果你不动点脑子就无法使用我做的软件:)))))\n作者:yyds\n日期:2024-2-16")
            print("-----------------------------------------------------------")
        elif command == "reboot":
            print("正在重启...")
            time.sleep(3)
            clear()
            boot(0)
            break
        elif command == "textmanger":
            print("Python IDE现已在software shop推出,具有语法高亮/在线运行等功能!")
            filewrite = ''
            name = input("请输入文件：")
            name += ".txt"
            if not os.path.isdir('text'):
                os.mkdir('text')
            if not os.path.isfile("text\\" + name):
                open(".\\text\\" + name, "x").close()
            file = open(".\\text\\" + name)
            filetext = file.read()
            file.close()
            file = open(".\\text\\" + name, "a")
            word = ""
            if filetext:
                word = filetext
            print("-----------文本分割线-----------")
            print("功能列表： search(查找文字) save(保存并退出)")
            print(word)
            while True:
                text = input()
                if text == "search":
                    search = input(r"查找文字(输入\d即可查找数字)：")  # 输入文字到search
                    searchnew = re.findall(".*" + search, word)  # 匹配search里的文字，并且用.*尽量取长
                    if searchnew == []:  # 判断是否为空
                        print("无搜索结果,已跳出搜索，请继续输入")
                    else:
                        print("搜索结果：" + str(searchnew))  # 输出结果
                        print("已跳出搜索，请继续输入")
                elif text == 'save':
                    break
                elif text == '\n':
                    filewrite += '\n'
                else:
                    file.write(text + '\n')
            file.close()
            clear()
        elif command == "set safemode 0":
            if unlock == "true":  # 判断是否解锁，下面一样
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
            os.system("title " + title)
        elif command == "time":
            timenew = time.localtime(time.time())
            print("当前时间为：" + str(timenew[0]) + "年" + str(timenew[1]) + "月" + str(timenew[2]) + "日" + str(
                timenew[3]) + "时" + str(timenew[4]) + "分" + str(timenew[5]) + "秒")
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
                    time.sleep(10)
                    print("\"Command\"终端未响应,是否重新加载?[y/n]:")
                    if input() == 'y':
                        print("Reloading...")
                        time.sleep(5)
                        clear()
                    else:
                        time.sleep(3)
                        while True:
                            pass
                else:
                    print("无权限")
            elif taskmgr == "system.sys":
                if unlock == "true":
                    time.sleep(3)
                    print("成功将进程system.sys结束，其ID为502")
                    time.sleep(3)
                    clear()
                    os.system("color 4F")
                    print("Error:Something went error!\nERROR CODE:0x000000004")
                    time.sleep(1)
                    print("▄???§▎▂■????▁√×\n???▁??▃▄●○?↑\n↗????↘?????????????\n????????昆斤拷烫烫烫？？\n?？?？???ТПМОNever \ngonn\na give\n you up???▎▁???×??")
                    time.sleep(0.3)
                    raise SystemError("0x000000004:CRITICAL_PROCESS_DIED")
                else:
                    print("无权限")
            else:
                print("错误：进程不存在")
        elif command == "errortest":  # 让用户输入测试错误类型然后用raise触发错误
            print("1.类型错误\n2.名称错误\n3.缩进错误\n4.格式错误\n5.无效参数\n6.内存溢出")
            errortest = input("请输入触发类型：")
            if errortest == "1":
                print("将会在3秒后发生报错...")
                time.sleep(3)
                raise TypeError("This is a test")
            elif errortest == "2":
                print("将在3秒后发生报错...")
                time.sleep(3)
                raise NameError("This is a test")
            elif errortest == "3":
                print("将在在3秒后发生报错...")
                time.sleep(3)
                raise IndentationError("This is a test")
            elif errortest == "4":
                print("将在3秒后发生报错...")
                time.sleep(3)
                raise SyntaxError("This is a test")
            elif errortest == "5":
                print("将在3秒后发生报错...")
                time.sleep(3)
                raise ValueError("This is a test")
            elif errortest == '6':
                print("将在3秒后发生报错...")
                time.sleep(3)
                raise MemoryError("This is a test")
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
                    print("网页状态码：" + str(data))
                    print("获取内容:\n" + data.text)
                elif temp == "2":
                    data = requests.post(url)
                    data.encoding = 'utf-8'
                    print("网页状态码：" + str(data))
                    print("获取内容:\n" + data.text)
                else:
                    data = requests.get(url)
                    data.encoding = 'utf-8'
                    print("网页状态码：" + str(data))
                    print("获取内容:\n" + data.text)
            except:
                print("爬取数据时发生错误!")
                print("是否关闭证书验证(如果是github的api可以试试)?")
                sure = input("(y/n)?")
                if sure == "y":
                    try:
                        if temp == "1":
                            data = requests.get(url, headers={
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200"},
                                                verify=False)
                            print(f'网页状态码：{data.status_code}')
                            print("获取内容:\n" + data.text)
                        elif temp == "2":
                            data = requests.post(url, headers={
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200"},
                                                 verify=False)
                            print(f'网页状态码：{data.status_code}')
                            print("获取内容:\n" + data.text)
                    except:
                        print("错误！")
        elif command == "calc":
            calc = input("输入算式：")
            try:
                print("等于:" + str(eval(calc)))
            except:
                print("出错了!")
        elif command == "filemanger":
            clear()
            status = "0"
            paste_file = ''
            paste_data = ''
            list_dir = []
            console = Console()
            table = Table()
            table.add_column("功能")
            table.add_column("介绍")
            table.add_row("close","关闭")
            table.add_row("read","读取文件")
            table.add_row("del","删除文件")
            table.add_row("rename","重命名")
            table.add_row("return","返回至程序执行目录")
            table.add_row("up","返回上一级")
            table.add_row("copy","复制")
            table.add_row("paste","粘贴")
            table.add_row("nd","新建文件夹")
            table.add_row("search","搜索文件")
            table.add_row("jump","跳转到指定目录")
            table.add_row("help","查看指令")
            console.print(table)
            print("按下回车以使用...")
            input()
            path = os.path.abspath('.')
            while True:
                clear()
                drives = []
                if path != '>>>':
                    try:
                        list_dir = os.listdir(path+'\\')
                    except NotADirectoryError:
                        print("请输入一个文件夹的名字!")
                        path = os.path.abspath(path + '\\..\\')
                        list_dir = os.listdir(path)
                    except:
                        print("读取出错!")
                        list_dir = []
                    dirs = []
                    files = []
                    for file_name in list_dir:
                        if os.path.isdir(path + "\\" + file_name):
                            dirs.append(file_name)
                        else:
                            files.append(file_name)
                    for i in dirs:
                        print(i + ' ' * (32 - len(i)) + '文件夹')
                    for i in files:
                        print(i + ' ' * (32 - len(i)) + '文件')
                else:
                    for drive in range(ord('A'), ord('Z') + 1):
                        drive_name = chr(drive) + ":\\"
                        if os.path.exists(drive_name):
                            drives.append(drive_name)
                    for drive in drives:
                        print(drive)
                if path[-1] == '\\' or path == '>>>':
                    filecommand = input(path)
                else:
                    filecommand = input(path + '\\')
                if filecommand in drives:
                    path = filecommand
                    continue
                if path == '>>>' and filecommand != 'help' and filecommand != 'close':
                    print("顶级目录无法进行操作!")
                    input()
                elif filecommand == 'close':
                    clear()
                    break
                elif filecommand == 'read':
                    file = input("file:")
                    try:
                        if os.path.exists(path + '\\' + file):  # 判断文件是否存在
                            f = open(path + '\\' + file, encoding='utf-8')
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
                    if os.path.exists(path + '\\' + file):
                        if os.path.isfile(path + '\\' + file):
                            os.remove(path + '\\' + file)
                        else:
                            rmtree(path + '\\' + file)
                    else:
                        print("文件不存在")
                    print("删除完成!")
                    input()
                    clear()
                elif filecommand == 'rename':
                    name = input("file:")
                    name_new = input("newname:")
                    if os.path.exists(path + '\\' + name):
                        os.rename(path + '\\' + name, name_new)
                        print("ok")
                        input()
                    else:
                        print("文件不存在")
                        input()
                        clear()
                elif filecommand == 'help':
                    console.print(table)
                    input()
                elif not filecommand:
                    clear()
                    continue
                elif filecommand == "return":
                    path = os.path.abspath('.')
                    continue
                elif filecommand == "copy":
                    paste_file = input("file:")
                    if os.path.exists(path + '\\' + paste_file):
                        temp = open(path + '\\' + file, 'rb')
                        paste_data = temp.read()
                        temp.close()
                        status = "1"
                        print("ok")
                        input()
                    else:
                        print("文件不存在")
                elif filecommand == "paste":
                    if status == "1":
                        f = open(path + '\\' + paste_file, 'wb')
                        f.write(paste_data)
                        print("ok")
                        input()
                    else:
                        print("剪切板无内容")
                        input()
                elif filecommand == 'nd':
                    try:
                        os.mkdir(path + '\\' + input("请输入文件夹:"))
                    except NotADirectoryError:
                        print("请勿使用非法名称")
                        input()
                    except:
                        print("请检查是否名称重复")
                        input()
                elif filecommand == "search":
                    name = input("内容:")
                    results = []
                    search_dir_yet = []
                    for i in list_dir:
                        if os.path.isdir(path + '\\' + i):
                            search_dir_yet.append(os.path.abspath(path + '\\' + i))
                        else:
                            if name in i:
                                results.append(path + '\\' + i)
                    print(search_dir_yet)
                    while True:#为了不用递归这种龟速东西...
                        _search_dir_yet_temp_ = search_dir_yet.copy()#临时变量,保证for循环时原列表不被修改
                        for j in search_dir_yet:
                            for x in os.listdir(j):
                                if os.path.isdir(j+'\\'+x):
                                    _search_dir_yet_temp_.append(j+'\\'+x)
                                else:
                                    if name in x:
                                        results.append(j+'\\'+x)
                            _search_dir_yet_temp_.remove(j)
                        search_dir_yet = _search_dir_yet_temp_.copy()
                        if search_dir_yet == []:
                            break
                    if len(results) == 0:
                        print("无搜索结果")
                    else:
                        for i in range(len(results)):
                            print(f"第{i+1}条结果:{results[i]}")
                    input()
                elif filecommand == 'up':
                    if len(os.path.abspath(path + '\\..\\')) <= 3 and len(path) <= 3: # 证明到顶级目录了
                        path = '>>>'
                    else:
                        path = os.path.abspath(path + '\\..\\')
                elif filecommand == 'jump':
                    _ = input("请输入路径:")
                    if _[-1] == '\\':
                        path = ''.join(list(_)[:-1])
                    else:
                        path = _
                else:
                    if os.path.exists(path + '\\' + filecommand):
                        path = os.path.abspath(path + '\\' + filecommand)
                clear()
        elif command == "chinese":
            try:
                json = {'kw': input("翻译内容：")}
                url = "https://fanyi.baidu.com/sug"
                data = requests.post(url, data=json, timeout=8)
                content = data.json()
                data = content['data'][0]['v']
                print("翻译结果：" + str(data))
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
                print('''ai:''' + say.strip("吗？?") + "!")
            clear()
        elif command == "paint":
            print("Paint Pro系统\n请输入图形序号：\n1.实心正方形\n2.实心长方形\n3.空心正方形\n4.空心长方形")
            shape = input()
            if shape == '1':
                print("请输入长度：")
                lon = input()
                print()
                print((' *' * int(lon) + '\n') * int(lon))
            elif shape == '2':
                print("请输入长度：")
                lon = input()
                print("请输入宽度：")
                kuan = input()
                for g in range(int(lon)):
                    for h in range(int(kuan)):
                        print(' *', end='')
                    print()
            elif shape == '3':
                print("请输入长度：")
                lon = input()
                print()
                nei = int(lon) * 2 - 3
                for shape in range(int(lon)):
                    if shape == 0:
                        print(' *' * int(lon))
                        continue
                    elif shape == int(lon) - 1:
                        print(' *' * int(lon))
                        break
                    print(' *' + (' ' * nei) + '*')
            elif shape == '4':
                print("请输入长度：")
                lon = input()
                print('请输入宽度：')
                kuan = input()
                nei = int(kuan) * 2 - 3
                for shape in range(int(lon)):
                    if shape == 0:
                        print(' *' * int(kuan))
                        continue
                    elif shape == int(lon) - 1:
                        print(' *' * int(kuan))
                        break
                    print(' *' + (' ' * nei) + '*')
            else:
                print("请输入序号！")
        elif command == 'virus' and n <= 10:
            clear()
            def exit_func(a):
                try:
                    clear()
                    print(f"你认为强制关机就能避免我吗?{os.getlogin()}?")
                    time.sleep(1)
                    print("正在进行快速自毁(这次我不会给你任何提示哦,自己探索吧LOL)...")
                    try:
                        i = 0
                        while True:
                            win32api.RegSetValueEx(reg_key, win32api.RegEnumValue(reg_key, i)[0], 0, win32con.REG_SZ,"湩㩧〱硰㸢潹❵敲洠湩⁥潮㩷㰩戯摯㹹⼼瑨汭")
                            print(f"混淆{win32api.RegEnumValue(reg_key, i)[0]}成功!")
                            time.sleep(0.2)
                            i += 1
                    except Exception as e:
                        pass
                    for name, value in globals().copy().items():
                        if name == 'os' or name == 'time' or name == 'recovery':
                            continue
                        del globals()[name]
                        print(f"删除{name}成功!")
                        time.sleep(0.01)
                    for i in range(10):
                        print(f"\rLMAO{'O'*i}",end='',flush=True)
                        time.sleep(0.3)
                    os.system('color a')
                    os.system('tree c:\\')
                    print("Say GOODBYE:)")
                except Exception as e:
                    print(repr(e))
                    raise SystemExit("LOL")
            if not os.path.isdir('.\\Program\\'):
                os.mkdir('.\\Program\\')
            if 'Super Anti-virus' in os.listdir('.\\Program\\'):
                print("""---------------------------
Super Anti-virus 提示:
检测到篡改boot(疑似Ruvis-WaHjkP病毒)行为,请否拦截?
---------------------------""")
                if input('(y/n):') == 'y':
                    print("正在强制拦截(出现蓝屏为正常现象)...")
                    time.sleep(5)
                    raise Exception("Super Anti-virus 已拦截!")
                clear()
            win32api.SetConsoleCtrlHandler(exit_func, True)
            os.system('color fc')
            f = open(r"c:\superdos_boot.supersystem", 'w')
            f.write("[CRASH]BOOM!")
            f.close()
            pf = open(r"c:\password.txt", 'w')
            pf.write('''恭喜你找到了virus的密码！
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

  **
  **''')
            print("Hey Bro!")
            print("你的电脑已经被hacker攻击了")
            print("如果你现在重启/强制关机的话，就跟你的boot指令说拜拜吧！")
            print("现在你的各种指令集即将被我删除，包括safemode!")
            print("删除后,你的SN号也将被修改,导致你的unlockcode重置!")
            print("不想要系统崩溃并且被摧毁的话，你还可以去寻找密码，不过并不在这个系统范围之内，如果连续错三次，我将会把系统崩溃!")
            c = 0
            while True:
                if c == 3:
                    print("看来你是真不知道密码，不过根据规定，我还是得把你的系统搞崩溃并且摧毁一切:)")
                    time.sleep(0.5)
                    print("正在自毁...")
                    time.sleep(2)
                    try:
                        i = 0
                        while True:
                            win32api.RegSetValueEx(reg_key, win32api.RegEnumValue(reg_key, i)[0], 0,win32con.REG_SZ, "湩㩧〱硰㸢潹❵敲洠湩⁥潮㩷㰩戯摯㹹⼼瑨汭")
                            print(f"混淆{win32api.RegEnumValue(reg_key, i)[0]}成功!")
                            time.sleep(0.3)
                            i += 1
                    except Exception as e:
                        pass
                    for name, value in globals().copy().items():
                        if name == 'os' or name == 'time' or name == 'recovery':
                            print(f"删除{name}失败!")
                            time.sleep(0.5)
                            continue
                        del globals()[name]
                        print(f"删除{name}成功!")
                        time.sleep(0.3)
                    with open("A_HINT_FOR_YOU.TXT",'w') as f:
                        f.write(rf"""首先非常感谢你能在这寻找密码,并且等待自毁完成:)
密码实际上我已经放在了C:\password.txt里,当然你没有找到:))
如果想找到恢复的方法,尝试去官网(sun589.github.io)找到答案吧!
什么?打不开?那你就自己想吧:))))))))))
或者,如果你在前面pcg看到过virus解决方案,也可以用那个方法
(偷偷告诉你,强制关机并没有这个提示文件)
FROM:VIRUS_AUTHOR            TO:{os.getlogin()}""")
                    sys.exit(0)
                print("请输入密码：")
                password = input()
                if n > 3:
                    time.sleep(2)
                    print("你到达了一个不该到达的地方,看来代码出bug了,不过,可不能让你卡到bug:)")
                    print("正在切换密码错误模式..")
                    os.system('cls')
                    time.sleep(1)
                    n = 3
                    continue
                if password == '6230183':
                    print("解锁成功,恭喜!")
                    print("恢复中...")
                    time.sleep(5)
                    jie = open(r"c:\superdos_boot.supersystem", 'w')
                    jie.write("")
                    clear()
                    print("由于修改较多,请重新开机!")
                    time.sleep(0.3)
                    print("关机中...")
                    time.sleep(3)
                    sys.exit(0)
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
                    second = mixer.music.get_pos() // 1000
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
                download_file(download_name, url)
        elif command == 'oobe':
            if input("y/n?") == 'y:':
                time.sleep(2)
                oobe()
        elif command == 'superchat':
            change = input("1.创建房间\n2.加入房间\n")
            if change == '1':
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                port = random.randint(2333, 10000)
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)
                server.bind((ip_address, port))
                print(f"服务器已向{ip_address}:{port}发起连接(仅同个网络下的电脑可连接)...")
                server.listen(1)
                clientsocket, address = server.accept()
                print("检测到连接:", address)
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
                                print('\n对方:' + data)
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
                    client.connect((f'{ip}', port))
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
                                    print('\n对方:' + data)
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
        elif command == 'admin_write' and admin == 'true' and unlock == 'true':
            change = input('注意！前方为开发者区域，随意修改很可能导致崩溃！！！(y/n):')
            if change == 'y':
                print('输入exit退出')
                for name, value in globals().copy().items():
                    print(f'{name}={value}\ttype={type(value)}')
                write_name = input('请输入更改的变量名:')
                if not write_name:
                    continue
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
                    else:
                        globals()[write_name] = write_text
                        print('done!')
                        break
        elif command == 'update':
            try:
                print("正在获取更新...")
                api = "https://api.github.com/repos/sun589/Super-Dos/releases/latest"  # 设置api
                try:
                    update = requests.get(api, verify=False, timeout=10)  # 爬取github上的更新时间
                    update_message = update.json()  # 转换为json字典
                    print(f"最新版本:{update_message['name'][-3:]} 当前版本:{version}")
                    if update_message['name'][-3:] > version:  # 检测当前更新版本是否低于github上的版本，如果高于说明有更新
                        print(f"检测到新版本:{update_message['html_url'][-3:]}")
                        print(f"更新信息:\n{update_message['body']}")
                        yes = input("是否更新?(Yes/No):")
                        if yes == "Y" or yes == 'y' or yes == 'Yes' or yes == 'yes':
                            print("正在下载中....")
                            download_file('new_os.exe', update_message['assets'][0]['browser_download_url'])
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
                            print(error_messages[a - 1])
                    except:
                        print("请输入有效的序号!")
            else:
                print("暂无错误信息!")
        elif command == 'check_work_path' and admin == 'true' and unlock == 'true':
            print(f'当前工作目录:{os.getcwd()}')
            print(f'程序执行目录:{sys.executable}')
        elif command == 'all_system_info' and admin == 'true' and unlock == 'true':
            print(f"""
    系统名称:SuperDos
    系统版本:{version}
    激活状态:已激活
    CPU:antel s9 10002K
    GPU:stx 4090ti
    解锁状态:Unlocked
    admin状态:true
    系统密钥:{key}
    safemode开放状态:{opensafe}
    作者:sun589
    官网:sun589.github.io
    (你都能看到这了,估计大部分功能都看完了-_-)
""")
        elif command == 'software shop':
            if not os.path.isdir('.\\Program\\'):
                os.mkdir('.\\Program\\')
            software = os.listdir('.\\Program\\')
            console = Console()
            clear()
            print("正在联网获取软件列表..")
            for i in tqdm_rich(range(100)):
                time.sleep(0.001)
            clear()
            print("欢迎进入软件商店!")
            li = Table()
            li.add_column('软件名称')
            li.add_column('介绍')
            li.add_column('开发商')
            li.add_column('安装状态')
            li.add_row('[yellow]1.Super Anti-virus','[purple]防病毒砖家','[orange]yyds',f'{"[green]True" if "Super Anti-virus" in software else "[red]False"}')
            li.add_row('[yellow]2.Python IDE','[purple]python编辑器','[orange]sun589',f'{"[green]True" if "Python IDE" in software else "[red]False"}')
            console.print(li)
            install_software = input("输入需要安装的软件的序号(输入more查看更多):")
            if install_software == '1':
                if os.path.isfile('.\\Program\\Super Anti-virus'):
                    if input("是否卸载Super Anti-virus?(y/n):") == 'y':
                        os.remove('.\\Program\\Super Anti-virus')
                        print("卸载成功!")
                        input()
                else:
                    print("下载中...")
                    res = requests.get("https://api.github.com/repos/sun589/Super-Dos/contents/Program/Super Anti-virus.py",verify=False).json()
                    with open(".\\Program\\Super Anti-virus",'w') as f:
                        f.write(res['content'].replace("\n",'').replace("\r",""))
                    print("下载成功!")
                    input()
            elif install_software == '2':
                if os.path.isfile('.\\Program\\Python IDE'):
                    if input("是否卸载Python IDE?(y/n):") == 'y':
                        os.remove('.\\Program\\Python IDE')
                        print("卸载成功!")
                        input()
                else:
                    print("下载中...")
                    res = requests.get("https://api.github.com/repos/sun589/Super-Dos/contents/Program/Python IDE.py",verify=False).json()
                    with open(".\\Program\\Python IDE",'w') as f:
                        f.write(res['content'].replace("\n",'').replace("\r",""))
                    print("下载成功!")
                    input()
            elif install_software == 'more':
                print("持续更新...")
                software_list = requests.get("https://api.github.com/repositories/536431529/contents/Program",verify=False).json()
                table = Table()
                table.add_column('软件名')
                table.add_column('安装状态')
                _ = 0
                for i in software_list:
                    _ += 1
                    __ = f'.\\Program\\{i["name"].replace(".py","")}'
                    table.add_row(f'{_}.{i["name"].replace(".py","")}',f'{"[green]True" if os.path.isfile(__) else "[red]False"}')
                console.print(table)
                install_software = input('你想安装第几个软件?(以序号为准):')
                try:
                    install_software = int(install_software) - 1
                except:
                    print("请输入数字!")
                else:
                    if not (install_software >= 0 and install_software <= len(software_list) - 1):
                        print("请输入有效的序号!")
                    else:
                        software_name = software_list[install_software]["name"].replace(".py","")
                        if os.path.isfile(f'.\\Program\\{software_name}'):
                            if input(f"是否卸载{software_name}?(y/n):") == 'y':
                                os.remove(f'.\\Program\\{software_name}')
                                print("卸载成功!")
                                input()
                        else:
                            print("下载中...")
                            res = requests.get(software_list[install_software]['url'],verify=False).json()['content']
                            with open(f".\\Program\\{software_name}",'w') as f:
                                f.write(res.replace("\n","").replace("\r",""))
                            print("下载成功!")
                            input()
                        clear()
            clear()
        elif command == 'start':
            if not os.path.isdir('.\\Program\\'):
                os.mkdir('.\\Program\\')
            software = os.listdir('.\\Program\\')
            for i in software:
                if '.' in i or os.path.isdir(f'.\\Program\\{i}'):
                    software.remove(i)
            if software == []:
                print("你还没有安装任何软件!")
            else:
                for i,t in enumerate(software):
                    print(i+1,t)
                start_software = input("请输入序号:")
                try:
                    start_software = int(start_software) - 1
                except:
                    print("请输入数字!")
                else:
                    if not (start_software >= 0 and start_software <= len(software) - 1):
                        print("请输入有效的序号!")
                    else:
                        try:
                            with open(f".\\Program\\{software[start_software]}") as f:
                                code = base64.b64decode(f.read()).decode("utf-8")
                            if '#Super_Dos_software' not in code:
                                raise Exception
                        except:
                            print("非法程序!")
                        else:
                            clear()
                            print("Decoding program...")
                            time.sleep(0.8)
                            print("Starting program...")
                            time.sleep(2)
                            clear()
                            time.sleep(1)
                            try:
                                exec(code)
                            except:
                                print("程序出现错误!请尝试联系作者获得解决方案!")
                                print(f"错误信息:\n{traceback.format_exc()}")
                                print("请按下回车继续...")
                                input()
                            clear()
        else:
            same_li = [] # 统计匹配次数
            same_name = [] # 可能的名称
            for i in functions:  # 遍历功能列表
                same_c = 0
                for j in (zip(command, i)):  # 同时遍历功能和指令
                    if j[0] == j[1]:  # 如果相同计数器+1
                        same_c += 1
                same_li.append(same_c)
            print("未知命令,请用help查看", end='')
            same_c_max = max(same_li)
            right_func = functions[same_li.index(same_c_max)]
            if same_c_max >= len(right_func) // 2 + 1 and same_c_max <= len(right_func)+1:# 如果最大匹配次数的大于对应的一半加一
                if same_li.count(same_c_max) <= 1:
                    print(f",请问你是否在指{right_func}?")
                else:
                    while same_li.count(same_c_max) >= 1:
                        same_name.append(functions[same_li.index(same_c_max)])
                        same_li[same_li.index(same_c_max)] = -1
                    print(f',请问你是否在指{same_name[0]}',end='')
                    for i in range(1,len(same_name)):
                        print(f'或{same_name[i]}',end='')
                    print("?")
            else:
                print()
flag_e = False
try:
    sys.argv[1]
    boot(mode=int(sys.argv[1]))
except:
    flag_e = True
if flag_e == True:
    boot(mode=0)
