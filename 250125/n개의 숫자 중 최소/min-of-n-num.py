n = int(input())
a = list(map(int, input().split()))

# Write your code here!
ele=min(a)
count=0
for i in range(n):
    if a[i]==ele:
        count+=1
print(min(a),count)
