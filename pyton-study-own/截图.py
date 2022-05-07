# 该脚本将简单地截取屏幕截图，而无需使用任何屏幕截图软件。

# 在下面的代码中，给大家展示了两种Python截取屏幕截图的方法。

# 方法①
from mss import mss
with mss() as screenshot:
    screenshot.shot(output='scr.png')

#保存到根目录本地文件

# # 方法②
# import PIL.ImageGrab
# scr = PIL.ImageGrab.grab()
# scr.save("scr.png")
