from tkinter import *
#Label(text='Spam').pack()
#mainloop() processing takes place here
from tkinter.messagebox import showinfo
def reply():
    showinfo(title='popup',message='Button Pressed')
window=Tk()
button=Button(window,text='press',command=reply)
#button.place(x = 100, y = 25)
button.pack()
window.mainloop()