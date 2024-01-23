import base64
from os import system
while True:
    try:
        key = input("Input your SN:")
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
        system('cls')
    except TypeError:
        print("Check your SN!Is it right?")
        input()
    except:
        print("Something went error!")
        print("Please try again!")
        input()