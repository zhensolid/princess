
# todo 使用Python的pikepdf模块，即可对文件进行加密，写一个循环就能进行批量加密文档。
# todo 如果你有100个或更多的PDF文件需要加密，手动进行加密肯定是不可行的，极其浪费时间。

# PDF加密
import pikepdf

pdf = pikepdf.open("test.pdf")
pdf.save('encrypt.pdf', encryption=pikepdf.Encryption(owner="your_password", user="your_password", R=4))
pdf.close()




# PDF解密
import pikepdf

pdf = pikepdf.open("encrypt.pdf",  password='your_password')
pdf.save("decrypt.pdf")
pdf.close()