n = int(input())
a = list(map(int, input().split()))

while n>0:
    ele=max(a)
    pos=a.index(ele)
    print(pos+1,end=' ')
    a=a[:pos]
    n=len(a)