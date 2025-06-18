m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
numberofdays=[0,31,28,31,30,31,30,31,31,30,31,30,31]
days=0
if m1<=m2:
    for i in range (m1,m2):
        #print(numberofdays[i])
        days+=numberofdays[i]
else:
    days=0 
days+=d2-d1
#print(days)
weekdays=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
thisday=days%7
days=days//7
if weekdays[thisday]==A:
    print(days+1)
else:
    print(days)
#print(weekdays[days])