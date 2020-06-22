from tkinter import *
top=Tk()

def show(event):
    cnvs.create_text(event.x,event.y,text="(",event.x,","+str(event.y)+")")
cnvs=Canvas(top,width=200,height=100)
cnvs.pack()
cnvs.bind('<Button-1>',show)
top.mainloop()
