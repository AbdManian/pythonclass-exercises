from tkinter import *
from tkinter.ttk import *
#from tkinter import filedialog
import passchecker

class MpscApplication(Frame):
    def __init__(self, master=None):
        self.master = master
        self.master.title("Ex4: Mahyar Password Strength Checker")
        self.cur_password = StringVar()
        self.cur_response = StringVar()
        self.cur_error = StringVar()

        Label(master, text='MPSC', font=(None, 18)).pack(side=TOP)

        frame1 = Frame(master)
        frame1.pack(fill=X)
        Label(frame1, text='Password', width=6).pack(side=LEFT, padx=5, pady=5)
        self.pass_entry = Entry(frame1, textvariable=self.cur_password)
        self.pass_entry.pack(fill=X, padx=5, pady=5)

        frame2 = Frame(master)
        frame2.pack(fill=X)
        Label(frame2, text='Mahyar', width=6).pack(side=LEFT, padx=5, pady=5)
        self.msg_resp = Message(frame2, text='....', anchor=W, width=130,
                textvariable=self.cur_response, bg='light sky blue')
        self.msg_resp.pack(fill=X, padx=5, pady=5)

        frame3 = Frame(master)
        frame3.pack(fill=X)
        Label(frame3, text='Error', width=6).pack(side=LEFT, padx=5, pady=5)
        self.msg_error = Message(frame3, text='....', anchor=W, width=130,
                textvariable=self.cur_error, bg='light sky blue')
        self.msg_error.pack(fill=X, padx=5, pady=5)

        framex = Frame(master)
        framex.pack(fill=X)

        Button(framex, text='About', width=5, command=self.about_clicked).pack(side=RIGHT, padx=5, pady=5)

        self.pass_entry.bind('<Key>', self.password_changed)


    def about_clicked(self):
        print("About is clicked")

    def password_changed(self, event):

        ret = passchecker.verify(self.cur_password.get())

        if type(ret) in (tuple, list) and len(ret)==2:
            pass_ok, error = ret
        else:
            pass_ok, error = ret, ""

        if pass_ok:
            self.cur_response.set("Password is ok")
            self.msg_error.config(bg='light sky blue')
            self.msg_resp.config(bg='light sky blue')
        else:
            self.cur_response.set("Password is nok")
            self.msg_error.config(bg='tomato')
            self.msg_resp.config(bg='tomato')

        self.cur_error.set(error)


if __name__ == '__main__':
    root = Tk()
    win = MpscApplication(root)
    root.mainloop()
