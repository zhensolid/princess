# -*- coding:utf-8 -*-
import time
from pynput.keyboard import Key, Controller


# 定义键盘控制器，用于控制键盘输入
keyboard = Controller()

# 设置按键的次数和按键的间隔时间
times = int(input("请输入按键的次数：")) 
interval = float(input("请输入按键的间隔时间(秒)："))

# 循环指定次数
for i in range(times):  # 模拟按键
    keyboard.press('a') 
    keyboard.release('a')
    # 间隔一段时间
    time.sleep(interval)
print("完成！")
