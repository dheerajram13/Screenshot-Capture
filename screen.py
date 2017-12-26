import pyautogui
from tkinter import *


def take():
       a= image_text.get()+"."+image_format.get()
       pyautogui.screenshot(a)
window  = Tk()
window.title("ScreenShot Capture")
window.geometry("250x70")
l1=Label(window,text='Image name: ')
l1.grid(row=0,column=0)
l1=Label(window,text=' Image Format: ')
l1.grid(row=1,column=0)
image_text = StringVar()
image_format = StringVar()
e1=Entry(window,textvariable=image_text)
e1.grid(row=0,column=1)
e1=Entry(window,textvariable=image_format)
e1.grid(row=1,column=1)
b1 = Button(window,text='Screenshot',width=12,command=take)
b1.grid(row=2,column=0,columnspan=2)
window.mainloop()
