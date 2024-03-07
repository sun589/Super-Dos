# 这里看起来似乎少了些东西(注意仔细观察合法程序代码,让我变成"合法程序")...
# 修改完代码后,你可以尝试研究下载完后Program目录程序的密文是由什么加密的,之后加密修改完的代码并篡改下载的程序
print("""
========================================================================
 /$$   /$$ /$$                  /$$$$$$$$                  /$$          
| $$  /$$/|__/                 |__  $$__/                 | $$          
| $$ /$$/  /$$ /$$$$$$$   /$$$$$$ | $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$$
| $$$$$/  | $$| $$__  $$ /$$__  $$| $$ /$$__  $$ /$$__  $$| $$ /$$_____/
| $$  $$  | $$| $$  \ $$| $$  \ $$| $$| $$  \ $$| $$  \ $$| $$|  $$$$$$ 
| $$\  $$ | $$| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$| $$ \____  $$
| $$ \  $$| $$| $$  | $$|  $$$$$$$| $$|  $$$$$$/|  $$$$$$/| $$ /$$$$$$$/
|__/  \__/|__/|__/  |__/ \____  $$|__/ \______/  \______/ |__/|_______/ 
                         /$$  \ $$                                      
                        |  $$$$$$/                                      
                         \______/    
                          For every hackers:)
========================================================================
""")
time.sleep(5)
while True:
    clear()
    print("""==============================
 1.系统状态        2.暴力解锁
 3.获取解锁码      4.强制Debug
 5.关于            6.退出
==============================""")
    choose = input("请输入需要的功能序号:")
    if choose == '1':
        print(f"Admin状态:{admin}")
        print(f"System解锁状态:{unlock}")
        print(f"Debug状态:{debug}")
        input()
    elif choose == '2':
        if admin == 'true' and unlock == 'true':
            print("您的系统无需破解!")
            input()
        else:
            if input("请确定是否强制解锁(y/n):") == 'y':
                print("破解中...")
                time.sleep(13)
                win32api.RegSetValueEx(reg_key, "unlock_status", 0, win32con.REG_SZ, "true")
                win32api.RegSetValueEx(reg_key, "oobe_status", 0, win32con.REG_SZ, "false")
                win32api.RegSetValueEx(reg_key, "admin_status", 0, win32con.REG_SZ, "true")
                print("破解成功,请重启应用设置!")
                input()
    elif choose == '3':
        print("generating...")
        a = 0
        for i in key:
            a += ord(i)
        a *= 1145141919
        a = str(a)
        unlockcode = base64.b32encode(a.encode('utf-8')).decode('utf-8')
        unlockcode = unlockcode.replace('=','')
        print(f"Success!")
        print(f"unlockcode:{unlockcode}")
        input()
    elif choose == '4':
        print("更改中..")
        time.sleep(6)
        debug = True
        print("修改成功!")
        input()
    elif choose == '5':
        print("""===============================
KingTools v1.0
作者:yyds
感谢你这位hacker使用本工具!
你可以尝试研究工具代码了解原理:)
===============================""")
        input()
    elif choose == '6':
        break
    else:
        print("请输入有效序号!")
