from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.replay)
        button.pack()
    def replay(self):
        showinfo(title='popup', message='Button pressed!')

if __name__  ==  '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()
