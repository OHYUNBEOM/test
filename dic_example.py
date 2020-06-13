def star():
    global cnt
    for j in range(cnt):
        print("*",end='')
c=input("문자열 입력 : ")
dic={}
cnt=0

for k in c:
    dic[k]=cnt
    cnt=cnt+1
    
for k in dic:
    cnt=0
    for n in c:
        if k==n:
            cnt=cnt+1
    print(k," : ",cnt,"회 l ",end='')
    star()
    print()
