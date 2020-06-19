from tkinter import *
top=Tk()
top.title='체크버튼'
cnvs=Canvas(top,width=500,height=200,bg='white')
cnvs.pack()
v1=IntVar()
v2=IntVar()
v3=IntVar()
def click():
    s=v1.get()
    s1=v2.get()
    s3=v3.get()
    if s==1:
        cnvs.create_rectangle(10,25,490,190)
    if s1==1:
        cnvs.create_oval(10,25,490,190)
    if s3==1:
        cnvs.create_line(10,25,490,190)
    if s==0 and s1==0 and s3==0:
        cnvs.delete('all')
         
cb1=Checkbutton(top,text='직사각형',variable=v1,command=click).pack(padx=50,side=LEFT)
cb2=Checkbutton(top,text='타 원 ',variable=v2,command=click).pack(padx=50,side=LEFT)
cb3=Checkbutton(top,text='직 선 ',variable=v3,command=click).pack(padx=50,side=LEFT)
top.mainloop()

        
    
