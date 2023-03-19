import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

# 创建窗口
window = tk.Tk()
window.title("信用卡记录软件")


# 添加标签和输入框
label1 = tk.Label(window, text="信用卡银行名称")
label1.pack()
# 创建下拉框
banks = ["工商银行", "中信银行", "光大银行", "广发银行", "平安银行", "招商银行"]
variable = tk.StringVar(window)
variable.set(banks[0])
option_menu = tk.OptionMenu(window, variable, *banks)
option_menu.pack()
label2 = tk.Label(window, text="消费金额")
label2.pack()
entry2 = tk.Entry(window,width=10)
entry2.pack()
label3 = tk.Label(window, text="消费日期")
label3.pack()
# 创建日期选择框
transaction_date = DateEntry(window, width=12, background='darkblue',
                             foreground='white', borderwidth=2, year=2023,
                             month=1, day=1)
transaction_date.pack()

# 连接数据库
try:
    mydb = mysql.connector.connect(
        host="1.117.233.127",
        user="kali",
        password="19841122Cy!",
        database="bank_card"
    )
except mysql.connector.Error as error:
    messagebox.showerror("Error", "数据库连接失败，请检查数据库配置。")
    window.destroy()

# 添加数据函数


def add_data():
    # 获取输入框的值
    credit_card = variable.get()
    amount = float(entry2.get())
    transaction_date_value = transaction_date.get_date().strftime('%Y-%m-%d')

    # 插入数据
    mycursor = mydb.cursor()
    sql = "INSERT INTO credit_card_transactions (credit_card_id, amount, transaction_date) VALUES ((SELECT id FROM credit_cards WHERE bank_name = %s), %s, %s)"
    val = (credit_card, amount, transaction_date_value)
    mycursor.execute(sql, val)

    # 提交更改
    mydb.commit()

    # 显示插入成功的消息
    messagebox.showinfo("Success", f"{mycursor.rowcount} 条记录插入成功。")

    # 清空输入框
    entry2.delete(0, tk.END)
    transaction_date.set_date("")

    # 关闭连接
    mycursor.close()
    mydb.close()


# 添加按钮
button_add = tk.Button(window, text="添加", command=add_data)
# 按钮距离调整
button_add.pack(side=tk.LEFT, padx=(40,10))

# 添加关闭按钮
button_close = tk.Button(window, text="关闭", command=window.destroy)
button_close.pack(side=tk.RIGHT, padx=(10,40))

# 运行窗口
window.mainloop()
