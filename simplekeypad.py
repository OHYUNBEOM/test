from tkinter import *
top=Tk()
lbls=[['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
for r in range(4):
    for c in range(3):
        Label(top,relief=RAISED,padx=10,text=lbls[r][c]).grid(row=r,column=c)
