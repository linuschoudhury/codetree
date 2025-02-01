a=input()
b=input()
count=0
for i in range(len(a)):
    a=a[-1]+a[:len(a)-1]
    count+=1
    if b==a:
        print(count)
        break
    elif count>=len(a):
        
        print(-1)
        break