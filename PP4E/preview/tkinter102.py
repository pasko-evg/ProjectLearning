from tkinter import *
from tkinter.messagebox import showinfo


class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, master=parent)
        button = Button(self, text='Press', command=self.reply)
        button.pack()
    def reply(self):
        showinfo(title='popup', message='Button pressed')

if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()
