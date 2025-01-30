n=int(input())
total=''
words=list(input().split())
for i in range(n):
    total+=words[i]
for i in range(0,len(total),5):
    print(total[i:i+5])