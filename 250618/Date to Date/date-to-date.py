m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


daydiff=d2-d1
monthdiff=0
for i in range(m1,m2):
    monthdiff+=num_of_days[i]
    #print(i, num_of_days[i])
result=max(daydiff+monthdiff+1,1)
print(result)
