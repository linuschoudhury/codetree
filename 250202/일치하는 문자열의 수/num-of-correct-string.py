n,a=input().split()
n=int(n)
count=0
for i in range(n):
    word=input()
    if word==a:
        count+=1
print(count)