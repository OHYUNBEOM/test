from tkinter import *
window=Tk()
window.title("라디오버튼과 체크버튼")
cnvs=Canvas(window,width=500,height=200,bg="white")
cnvs.pack()
rbch=IntVar()
cbch1=IntVar()

def pic():
    shape=rbch.get()
    if shape==1:
        cnvs.delete("all")
        cnvs.create_rectangle(10,25,490,190)
    if shape==2:
        cnvs.delete("all")
        cnvs.create_oval(10,25,490,190)
    if shape==3:
        cnvs.delete("all")
        cnvs.create_line(10,25,490,190)

def color():
    shape=cbch1.get()
    if shape==1:
        cnvs.create_rectangle(10,25,490,190,fill="pink")
    if shape==2:
        cnvs.create_oval(10,25,490,190,fill="pink")

radio1=Radiobutton(window,text="직사각형",variable=rbch,value=1,command=pic)
radio2=Radiobutton(window,text="타 원",variable=rbch,value=2,command=pic)
radio3=Radiobutton(window,text="직 선",variable=rbch,value=3,command=pic)
cb1=Checkbutton(window,text="색채우기",variable=cbch1,command=color)

radio1.pack(padx=25,side=LEFT)
radio2.pack(padx=25,side=LEFT)
radio3.pack(padx=25,side=LEFT)
cb1.pack(padx=25,anchor=W)

window.mainloop()
