from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import database


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Ex3: Parking Controller!")
        self.details_var = IntVar()

        self.grid(row=0, column=0, sticky=W+E+N+S)


        l_main_list = Label(self, text='Vehicles in Parking')
        data = Listbox(self)
        l_add = Label(self, text='Add New')
        entry_add = Entry(self)
        b_add = Button(self, text='Add', command=self.call_add)
        l_remove = Label(self, text='Remove')
        b_remove_first = Button(self, text='First Item', command=self.call_remove_first)
        b_remove_last = Button(self, text='Last Item', command=self.call_remove_last)
        l_find = Label(self, text='Find')
        entry_find = Entry(self)
        l_find_answer = Label(self, text='-'.center(12))
        l_add_multiple = Label(self, text='Add Multiple')
        entry_add_multiple = Entry(self)
        b_add_multiple = Button(self, text='Add', command=self.call_add_multiple)
        l_export = Label(self, text='Export')
        b_save_to_file = Button(self, text='Save to file', command=self.call_save_to_file)
        l_import = Label(self, text='Import')
        b_import_from_file = Button(self, text='Load from file', command=self.call_load_from_file)
        details = Checkbutton(self, text='Show details', command=self.detail_changed, var=self.details_var)

        # Place all widgets on the form
        l_main_list.grid(row=0, column=0, columnspan=3, sticky=W)
        data.grid(row=1, column=0, columnspan=3, sticky=W+E)
        l_add.grid(row=2, column=0, sticky=W)
        entry_add.grid(row=2, column=1)
        b_add.grid(row=2, column=2, sticky=E+W)
        l_remove.grid(row=3, column=0, sticky=W)
        b_remove_first.grid(row=3, column=1, sticky=E+W)
        b_remove_last.grid(row=4, column=1, sticky=E+W)

        l_find.grid(row=5, column=0, sticky=W)
        entry_find.grid(row=5, column=1)
        l_find_answer.grid(row=5, column=2, sticky=E)
        l_add_multiple.grid(row=6, column=0, sticky=W)
        entry_add_multiple.grid(row=6, column=1)
        b_add_multiple.grid(row=6, column=2, sticky=E+W)
        l_export.grid(row=7, column=0, sticky=W)
        b_save_to_file.grid(row=7, column=1, sticky=W+E)
        l_import.grid(row=8, column=0, sticky=W)
        b_import_from_file.grid(row=8, column=1, sticky=W+E)
        details.grid(row=9, column=0, sticky=E, columnspan=3)

        self.data = data
        self.entry_add = entry_add
        self.entry_find = entry_find
        self.find_answer = l_find_answer
        self.entry_add_multiple = entry_add_multiple
        self.entry_find.bind('<Key>', self.find_keypress)

        self.update_list()

    def find_keypress(self, event):
        if event.char=='\r':
            lookup = database.db_find(self.entry_find.get())
            if lookup:
                self.find_answer.config(text='Available')
            else:
                self.find_answer.config(text='Not Found!')
            print(lookup)

    def detail_changed(self):
        self.update_list()

    def update_list(self):
        self.data.delete(0, END)
        cnt = 0
        for x in database.db:

            if self.details_var.get():
                text = "{0:2}: <{1}>".format(cnt, x)
            else:
                text = x
            self.data.insert(END, text)
            cnt += 1

    def call_save_to_file(self):
        filename = filedialog.asksaveasfilename(title='Export vehicle list', defaultextension='txt',
                                                filetypes=(("text files", "*.txt"), ("all files", "*.*")))

        database.db_export_to_file(filename)
        self.update_list()

    def call_load_from_file(self):
        filename = filedialog.askopenfilename(title='Import vehicle list from file', defaultextension='txt',
                                              filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        database.db_import_from_file(filename)
        self.update_list()

    def call_add(self):
        database.db_add(self.entry_add.get())
        self.update_list()

    def call_remove_first(self):
        database.db_remove_first()
        self.update_list()

    def call_remove_last(self):
        database.db_remove_last()
        self.update_list()

    def call_add_multiple(self):
        value_list = self.entry_add_multiple.get()
        database.db_add_multiple(value_list)
        self.update_list()


if __name__ == '__main__':
    root = Tk()
    win = Window(root)
    root.mainloop()
