from tkinter import *
from tkinter.messagebox import showinfo
from OOPSGUI import MyGUI
#main app window
mainwin=Tk()
Label(mainwin,text=__name__).pack()
#popup window
popup=Toplevel()
Label(popup,text='Attach').pack(side=LEFT)
MyGUI(popup).pack(side=RIGHT) ## passing instance to class, we can invoke functions by either object or by using classname and passing instance
mainwin.mainloop()