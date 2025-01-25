n = int(input())
a = list(map(int, input().split()))

# Write your code here!
ele=max(a)
print(ele,end=' ')
#print(a)
a.remove(ele)
print(max(a))
