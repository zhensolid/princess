from wxpy import *
from time import sleep
import random
bot = Bot(cache_path= True)
#print('防止微信账号违规操作被封，每次发送信息时间间隔为随机0-1.5s')
message = input('请输入要发送的微信信息：')
friends_number = input('请输入账号好友数量：')
number = int(friends_number)
accord = input('输入符合条件人的关键字(如要发送全部好友，请输入all)：')
accordint= str(accord)
for i in range(0, number):
    try:
        my_friend = bot.friends(update=True).search()[i]
    except Exception as b:
        print('好友没有uid或查找好友超过索引数')
else:
    print(my_friend)
people = str(my_friend)
if accordint in people:#如果备注信息包含你输入的文字
    try:
        print('找到符合要求的好友')#打印好友备注
        my_friend.send(message)#发送信息
    except Exception as a:#如果执行出错
        print("不是您的好友或不存在该好友")
else:
    print('发送信息成功')
loadtime = random.uniform(0.5, 1.5)
sleep(loadtime)
print(loadtime)
#try执行成功
if accordint == 'all':#如果备注信息包含你输入的文字
    try:
        print(my_friend)#打印好友备注
        my_friend.send(message)#发送信息
    except Exception as a:#如果执行出错
        print("好友不是您的好友或不存在该好友")
else:
    print('发送信息成功')#try执行成功
print('已完成')
bot.logout()
bot.join()