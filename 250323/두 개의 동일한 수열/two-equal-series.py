n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
if A.sort()==B.sort():
    print('Yes')
else:
    print('No')
