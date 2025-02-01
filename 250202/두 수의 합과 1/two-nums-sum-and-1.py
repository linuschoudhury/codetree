a,b=input().split()
a=int(a)
b=int(b)
total=str(a+b)
count=0
for char in total:
    if char == '1':
        count+=1
print(count)