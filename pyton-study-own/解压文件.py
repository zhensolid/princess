
# ? 使用zipfile模块进行文件解压，同理也可以对文件进行压缩。

# 解压文件
from zipfile import ZipFile

unzip = ZipFile("file.zip", "r")
unzip.extractall("output Folder")