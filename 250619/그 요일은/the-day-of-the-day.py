m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
numberofdays=[0,31,28,31,30,31,30,31,31,30,31,30,31]
days=0
if m1==m2:
    days=d2-d1
else:
    
    for i in range(m1,m2):
        days+=numberofdays[i]
    days+=d2-d1
#print(days)
days+=1
weekday=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
#print(weekday[days%7])
#for i in range(days):
    #print(weekday[i%7])
if days%7==1:
    print((days//7)+1)
    #print('fuck')
else:
    print((days//7))

