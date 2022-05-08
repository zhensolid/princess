import random

x = random.randint(0,10)

count = 0
while True:
    count += 1
    try:
        c = int(input('请猜测数字（0-10）'))
        if c > x:
            print("数字过大")
        elif c < x:
            print("数字过小")
        else:
            print("恭喜你才对了")
            break
    except:
        print("请输入正确的数字")

print("你一共猜出了%d次" % count)