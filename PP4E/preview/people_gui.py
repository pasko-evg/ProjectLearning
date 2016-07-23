from tkinter import *
from tkinter.messagebox import showinfo
import shelve

shelve_name = 'class-shelve'
field_names = ('name', 'age', 'job', 'pay')


def make_widgets():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    return window


db = shelve.open(shelve_name)
window = make_widgets()
window.mainloop()
db.close()
