n=int(input())
arr=[]
count=0
total=0
for i in range(n+1):
    word=input()
    arr.append(word)
for i in range(n):
    if arr[i][0]==arr[-1]:
        count+=1
        total+=len(arr[i])
print("%d %.2f"%(count,total/count))