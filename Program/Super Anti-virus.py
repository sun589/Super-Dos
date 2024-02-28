#Super_Dos_software
print("欢迎使用Super Anti-virus!")
if time.time() % 35 == 0:
    print("更新最新病毒库...")
    time.sleep(4)
if input("是否进行扫描?(y/n):") == 'y':
    for x in range(1000000, 1001230):
        print(f"\r正在扫描0x{str(x).rjust(7, '0')}",end='',flush=True)
        time.sleep(0.00001)
        x += 3
    dangerous_files = []
    if os.path.isdir("Program"):
        for i in os.listdir('.\\Program\\'):
            print(f"\r正在扫描{i}",end='',flush=True)
            if '.' not in i and os.path.isfile(f'.\\Program\\{i}'):
                with open(f".\\Program\\{i}") as f:
                    try:
                        if '#Super_Dos_software' not in base64.b64decode(f.read()).decode("utf-8"):
                            dangerous_files.append(i)
                    except:
                        dangerous_files.append(i)
        clear()
    if dangerous_files != []:
        if input(f"检测到{len(dangerous_files)}个非法软件,是否处理?(y/n):") == 'y':
            print("删除中...")
            for i in dangerous_files:
                if os.path.isfile(f'.\\Program\\{i}'):
                    os.remove(f'.\\Program\\{i}')
            print("删除成功!")
    if n <= 10:
        if input("检测到编号Ruvis-WaHjkP病毒,是否立即清除?(y/n):") == 'y':
            print("修复中...")
            time.sleep(5)
            n = 77
            with open(r"c:\superdos_boot.supersystem",'w') as f:
                f.write('')
            print("已修复并安装防攻击补丁,请重启应用更新!")
    if n > 10 and dangerous_files == []:
        print("未发现任何病毒!")
    input()
