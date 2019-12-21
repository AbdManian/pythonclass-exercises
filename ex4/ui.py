from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo

class MpscApplication(Frame):
    def __init__(self, master, checker_method):
        self.master = master
        self.master.title("Ex4: Mahyar Password Strength Checker")
        self.cur_password = StringVar()
        self.cur_response = StringVar()
        self.cur_error = StringVar()
        self.checker_method = checker_method

        Label(master, text='MPSC', font=(None, 18)).pack(side=TOP)

        frame1 = Frame(master)
        frame1.pack(fill=X)
        Label(frame1, text='Password', width=9).pack(side=LEFT, padx=5, pady=5)
        self.pass_entry = Entry(frame1, textvariable=self.cur_password)
        self.pass_entry.pack(fill=X, padx=5, pady=5)

        frame3 = Frame(master)
        frame3.pack(fill=X)
        Label(frame3, text='Error', width=9).pack(side=LEFT, padx=5, pady=5)
        self.msg_error = Message(frame3, text='....', anchor=W, width=130,
                textvariable=self.cur_error, bg='light sky blue')
        self.msg_error.pack(fill=X, padx=5, pady=5)

        frame4 = Frame(master)
        frame4.pack(fill=X)
        Label(frame4, text='Quality', width=9).pack(side=LEFT, padx=5, pady=5)
        self.quality = Progressbar(frame4)
        self.quality.pack(fill=X, padx=5, pady=5)

        framex = Frame(master)
        framex.pack(fill=X)

        Button(framex, text='About', width=6, command=self.about_clicked).pack(side=RIGHT, padx=5, pady=5)

        self.pass_entry.bind('<Key>', self.password_changed)


    def about_clicked(self):
        with open('readme.txt', 'r') as f:
            rules = f.read()

        showinfo("About","Mahyar Password Strength Checker\nV 0.1\n\n" + rules)

    def password_changed(self, event):
        if event.char != '\r':
            return

        ret = self.checker_method(self.cur_password.get())

        pass_ok, error, q = ret

        self.quality.configure(value=q)

        if pass_ok:
            msg = "Password is ok"
            color = 'light sky blue'
        else:
            msg = "Invalid Password"
            color = 'tomato'

        self.cur_response.set(msg)
        self.msg_error.config(bg=color)

        self.cur_error.set(error)



def get_ui_root(checker_method):
    root = Tk()
    MpscApplication(root, checker_method)
    return root
