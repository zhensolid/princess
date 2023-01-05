import tkinter

#定义类
class Weblog(object):
#定义函数
    def login():
        print("登陆成功")

    def cancel():
        print("取消登陆")

    def loginwin():
        win = tkinter.Tk()
        win.title("登陆窗口")
        win.geometry("400x200")

        tkinter.Label(win, text="用户名：").place(x=50, y=50)
        tkinter.Label(win, text="密码：").place(x=50, y=90)

        var_usr_name = tkinter.StringVar()
        var_usr_name.set("admin")
        entry_usr_name = tkinter.Entry(win, textvariable=var_usr_name)
        entry_usr_name.place(x=160, y=50)

        var_usr_pwd = tkinter.StringVar()
        entry_usr_pwd = tkinter.Entry(win, textvariable=var_usr_pwd, show='*')
        entry_usr_pwd.place(x=160, y=90)
#调用定义函数Weblog.login
        btn_login = tkinter.Button(win, text="登陆", command=Weblog.login)
        btn_login.place(x=50, y=130)

        btn_cancel = tkinter.Button(win, text="取消", command=Weblog.cancel)
        btn_cancel.place(x=160, y=130)

        win.mainloop()
#调用定义函数
Weblog.loginwin()

