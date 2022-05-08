import random

x = random.randint(1,100)
counter = 0;
while True:
    counter += 1                                         #counter = counter + 1
    try:                                                 #使用try和except来避免输入异常
        number = int(input("请输入数字，范围(0-100)"))    #输入数字必须为数字，需要放在while内才能循环
        if number < x:
            print('输入数字为%d,数字小' % number)
        elif number > x:
            print('输入数字为%d,数字大' % number)
        else:
            print('恭喜你猜对了，正确数字为%d' % number)
            break                                        #跳出循环
    except:
        print('请输入数字！！！')

print("你一共才%d" % counter)
if counter > 7:
    print('你智商不足')
else:
    print('你真聪明')

input('Press Enter to exit…')