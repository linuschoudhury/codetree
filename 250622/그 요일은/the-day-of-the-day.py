m1, d1, m2, d2 = map(int, input().split())
A = input()
# Please write your code here.
numberofdays=[0,31,29,31,30,31,30,31,31,30,31,30,31]
days=0
if m1==m2:
    days=d2-d1
else:
    for i in range(m1,m2):
        days+=numberofdays[i]
    days+=d2-d1
days+=1
weekday=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
#print(days)
numberofweeks=days//7
extradays=days%7
if weekday.index(A)<=extradays-1:
    numberofweeks+=1
print(numberofweeks)

