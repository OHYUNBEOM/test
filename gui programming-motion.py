from tkinter import *
top=Tk()
oldx,oldy=0,0
def begin(event):
    global oldx,oldy
    oldx,oldy=event.x,event.y
def draw(event):
    global oldx,oldy,cnvs
    newx,newy=event.x,event.y
    cnvs.create_line(oldx,oldy,newx,newy)
    oldx,oldy=newx,newy
cnvs=Canvas(top,width=500,height=200,bg='lightgreen')
cnvs.pack()
cnvs.bind('<Button-1>',begin)
cnvs.bind('<Button1-Motion>',draw)

top.mainloop()
