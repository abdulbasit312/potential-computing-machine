from tkinter import *
from tkinter.messagebox import showinfo
from OOPSGUI import MyGUI
class Custom(MyGUI):
    def reply(self):
        showinfo(title='popup',message='Ouch!')
if __name__=='__main__':
    Custom().pack()
    mainloop()