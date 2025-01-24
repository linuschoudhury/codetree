arr=list(map(int,input().split()))

for i in range(2,11):
    arr.append(arr[i-1]+2*arr[i-2])

for j in range(10):
    print(arr[j],end=' ')

'''
terms = [a1, a2]
for i in range(2, n):
    terms.append(terms[i-1] + 2*terms[i-2])
'''