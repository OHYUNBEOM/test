from tkinter import *
top=Tk()
cnt=0
def stopwatch():
    if running:
        global cnt
        cnt+=1
        lb1.config(text=str(cnt))
    top.after(1000,stopwatch)
def start():
    global running
    running=True
def stop():
    global running
    running=False
def reset():
    global cnt
    cnt=0
    lb1.config(text=str(cnt))
lb1=Label(top)
lb1.pack()

running=False
stopwatch()
bt1=Button(top,text='start',width=25,command=start).pack()
bt2=Button(top,text='Stop',width=25,command=stop).pack()
bt3=Button(top,text='Reset',width=25,command=reset).pack()
top.mainloop()
