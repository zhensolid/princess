import mysql.connector
import tkinter as tk

# 创建窗口
window = tk.Tk()

# 添加标签和输入框
label1 = tk.Label(window, text="信用卡银行名称")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()
label2 = tk.Label(window, text="消费金额")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()
label3 = tk.Label(window, text="消费日期（格式为 YYYY-MM-DD）")
label3.pack()
entry3 = tk.Entry(window)
entry3.pack()

# 连接数据库
mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

# 添加数据函数
def add_data():
    # 获取输入框的值
    credit_card = entry1.get()
    amount = float(entry2.get())
    transaction_date = entry3.get()
    
    # 插入数据
    mycursor = mydb.cursor()
    sql = "INSERT INTO credit_card_transactions (credit_card_id, amount, transaction_date) VALUES ((SELECT id FROM credit_cards WHERE bank_name = %s), %s, %s)"
    val = (credit_card, amount, transaction_date)
    mycursor.execute(sql, val)
    
    # 提交更改
    mydb.commit()
    
    # 输出结果
    print(mycursor.rowcount, "记录插入成功。")
    
    # 关闭连接
    mycursor.close()
    mydb.close()

# 添加按钮
button = tk.Button(window, text="添加", command=add_data)
button.pack()

# 运行窗口
window.mainloop()
