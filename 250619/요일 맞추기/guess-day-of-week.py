m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

numberofdays=[0,31,28,31,30,31,30,31,31,30,31,30,31]
days=0

for i in range (1,m2):
    days+=numberofdays[i]
    

daysfromdate=d2-d1
#days+=daysfromdate
#print(days)
weekdays=['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
days=days%7
print(weekdays[days])