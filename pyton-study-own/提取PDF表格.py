# 有的时候，我们需要从PDF中提取表格数据。

# 第一时间你可能会先想到手工整理，但是当工作量特别大，手工可能就比较费劲。

# 然后你可能会想到一些软件和网络工具来提取 PDF 表格。

# 下面这个简单的脚本将帮助你在一秒钟内完成相同的操作。

# 方法①
import camelot

tables = camelot.read_pdf("tables.pdf")
print(tables)
tables.export("extracted.csv", f="csv", compress=True)

# 方法②, 需要安装Java8
# import tabula

# tabula.read_pdf("tables.pdf", pages="all")
# tabula.convert_into("table.pdf", "output.csv", output_format="csv", pages="all")
