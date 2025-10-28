n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
arr=[]
for i in range(n):
    arr.append((x[i],c[i]))
arr.sort(key=lambda t: t[0])

def weight(ch):
    return 1 if ch == 'G' else 2

left = 0
right = 0
total = 0
maxtotal = 0

while right < n:
    while right < n and arr[right][0] - arr[left][0] <= k:
        total += weight(arr[right][1])
        right += 1
    if total > maxtotal:
        maxtotal = total
    total -= weight(arr[left][1])
    left += 1
    if left > right:
        right = left

print(maxtotal)
