n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Write your code here!
def sublist(x,y):
    matched=False
    for i in range(len(a)):
        if b[0]==a[i]:
            matched=True
            for j in range(len(b)):
                if b[j]!=a[i+j]:
                    matched=False
                    break
    if matched==True:
        return 'Yes'
    else:
        return 'No'
print(sublist(a,b))