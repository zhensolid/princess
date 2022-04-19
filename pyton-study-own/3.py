import xlwt
# 导入第三方模块
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
#调用Workbook来创建excel表格类型，第一个参数是设置编码类型，第二个设置是否压缩
sheet = book.add_sheet("豆瓣电源TOP250",cell_overwrite_ok=True)
#用book对象调用add_sheet方法来创建sheet表格
#第一个参数是设置sheet名称
#第二个参数是设置cell单元是否可以用于重设值
col = ('电影详情链接','图片链接','影片中文名','影片外国名','评分','评价数','概况','相关信息','个人备注')
#用一个元组col自定义列的数量以及各列的属性名
for i in range(0,9):
    sheet.write(0,i,col[i])
#用for循环将col元组的元组值写入sheet，调用write
#第一个参数是行，第二个参数是列，第三个是元组值
#因为是列名，所以是第一行
savepath = 'C:/Users/Administrator/Desktop/excel.xls'
#实用savepath定义保存路径
book.save(savepath)
#实用book保存文件