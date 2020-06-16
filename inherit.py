class Queue:
    def __init__(self,lst=[]):
        self.lst=[]

    def addqueue(self,add):
        self.lst.append(add)

    def queue(self):
        print(self.lst)
        
    def delqueue(self):
        self.lst=self.lst[1:]
a=Queue()
a.addqueue(10)
a.addqueue(20)
a.queue()
a.delqueue()
a.queue()
