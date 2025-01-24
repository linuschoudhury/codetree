arr=input().split()
a,b=int(arr[0]),int(arr[1])
terms = [a, b]
for i in range(2, 11):
    terms.append(terms[i-1] + 2*terms[i-2])
for i in range(10):
    print(terms[i],end=' ')