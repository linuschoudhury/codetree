total=0
n=int(input())
for i in range(n):
    num=int(input())
    total+=num
total=str(total)
#print(total)
print(total[1:len(total)]+total[0])