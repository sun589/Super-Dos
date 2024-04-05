# Super_Dos_software
console = Console()
if not os.path.isdir('.\\py'):
  os.mkdir('.\\py\\')
table = Table()
table.add_column("文件名")
for i in os.listdir('.\\py\\'):
  table.add_row(i)
console.print(table)
py_file = input('请输入py文件名称(从当前目录的py文件夹下读取/新建):')
if py_file == '':
  print("检测到未输入内容!")
else:
  if not os.path.isfile(f'.\\py\\{py_file}'):
      open(f".\\py\\{py_file}", 'x').close()
  table_help = Table()
  table_help.add_column('功能')
  table_help.add_column('介绍')
  table_help.add_row(':help', '帮助')
  table_help.add_row(':wq','保存退出')
  table_help.add_row(':run', '运行')
  table_help.add_row(':del_line', '删除上一行')
  table_help.add_row(':remove_all', '删除所有内容')
  table_help.add_row(':change_file', '切换文件')
  table_help.add_row(':write_line', '切换到指定行写入内容(写完后指针将重新回到结尾)')
  line = -1
  while True:
      clear()
      code = open(f".\\py\\{py_file}", 'a+', encoding='utf-8')
      lines = 0
      code.seek(0, 0)
      for i in code:
          lines += 1
      code.seek(0, 0)
      _ = code.readlines()
      if not ('#!no_help_hint' in _ or '#!no_help_hint\n' in _):
          print("输入:help查看功能列表(如不想显示请在代码开头加上\"#!no_help_hint\")")
      if lines > 0:
          code.seek(0, 0)
          syntax = Syntax(code.read(), "python", theme="monokai", line_numbers=True)
          console = Console()
          console.print(syntax)
      console.print(f'{f"({line+1} line)" if line != -1 else ""}[red]>>>', end='')
      input_code = input()
      if input_code == ':wq':
          clear()
          break
      elif input_code == ':run':
          code.seek(0, 0)
          clear()
          local_vars = {}
          print('Ctrl+C 退出')
          print("---------------程序已开始---------------")
          try:
              exec(code.read(), local_vars)
          except KeyboardInterrupt:
              pass
          except Exception as e:
              print("程序出现报错!")
              print(f"错误信息:{traceback.format_exc()}")
          print("---------------程序已结束---------------")
          del local_vars
          print("输入1以回到ide,否则保存退出")
          if input() == '1':
              clear()
              continue
          else:
              break
      elif input_code == ':del_line':
          code.seek(0, 0)
          if lines > 1:
              y_code = code.readlines()[:-1]
              y_code[-1] = y_code[-1].replace('\n', '')
              code.truncate(0)
              code.seek(0, 0)
              code.write(''.join(y_code))
              code.close()
          else:
              code.truncate(0)
              code.close()
      elif input_code == ':remove_all':
          if input("你确定吗,这将删除所有内容!(y/n)") == 'y' and input('真的真的确定吗?(y/n)') == 'y':
              try:
                  print("你现在有5秒后悔时间,如果不想清除请按下Ctrl+C!")
                  for i in range(1, 6):
                      time.sleep(1)
                      print(f'..{i}')
                  print("清除中..")
                  code.truncate(0)
              except:
                  print('已撤销操作!')
      elif input_code == ':change_file':
          clear()
          table = Table()
          table.add_column("文件名")
          for i in os.listdir('.\\py\\'):
              table.add_row(i)
          console.print(table)
          py_file = input('请输入py文件名称(从当前目录的py文件夹下读取/新建):')
      elif input_code == ':write_line':
          try:
              line = int(input("输入行数:"))-1
              if line+1 <= 0 or (lines < 1 and line+1 > 1):
                  raise Exception
              insert_ = int(input('选择操作(1.插入 2.覆盖):'))
              print(insert_)
              if insert_ != 1 and insert_ != 2:
                  raise Exception
              if '#!no_help_hint' not in code.readlines() and insert_ == 2:
                  print("提示:留空可删除指定行(如不想显示请在代码开头加上\"#!no_help_hint\")")
                  input()
              code.seek(0,0)
              code.readlines()[line]
          except Exception as e:
              insert_ = 1
              line = -1
              print("请输入内容!")
              input()
      elif input_code == ':help':
          console.print(table_help)
          input()
      else:
          code.seek(0, 2)
          try:
              if input_code[0] == ':':
                  print("请输入有效指令!")
                  input()
                  continue
          except:
              pass
          if line != -1:
              code.seek(0, 0)
              y_code = code.readlines()
              _ = '\n'
              if insert_ == 2:
                  y_code[line] = input_code+f'{_ if lines >= 1 else ""}'
              else:
                  y_code.insert(line,input_code+f'{_ if lines >= 1 else ""}')
              code.truncate(0)
              code.seek(0, 0)
              code.write(''.join(y_code))
              code.close()
              line = -1
              continue
          if lines > 0:
              code.write('\n' + input_code)
          else:
              code.write(input_code)
          code.close()
          del code
