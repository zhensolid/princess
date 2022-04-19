from faker import Faker

import xlwt

fake = Faker("zh_CN")

book = xlwt.Workbook(encoding='utf-8',style_compression=0)

sheet = book.add_sheet("FAKER",cell_overwrite_ok=True)

col = ('姓名','电话号码','身份证','地址')
#用一个元组col自定义列的数量以及各列的属性名
for i in range(0,4):
    sheet.write(0,i,col[i])
#用for循环将col元组的元组值写入sheet，调用write
#第一个参数是行，第二个参数是列，第三个是元组值
#因为是列名，所以是第一行

for aa in range(1,10):
    #! aa循环第一个参数行数
    sheet.write(aa,0,fake.name())
    sheet.write(aa,1,fake.phone_number())
    sheet.write(aa,2,fake.ssn(min_age=18, max_age=90))
    sheet.write(aa,3,fake.address())



savepath = 'C:/Users/Administrator/Desktop/faker.xls'
#实用savepath定义保存路径
book.save(savepath)
#实用book保存文件