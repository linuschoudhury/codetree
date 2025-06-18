m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

numberofdays=[0,31,28,31,30,31,30,31,31,30,31,30,31]
days=0
for i in range (m1,m2):
    days+=numberofdays[i]
    #print(numberofdays[i])

daysfromdate=d2-d1
days+=daysfromdate
#print(days)
weekdays=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
days=days%7
print(weekdays[days])