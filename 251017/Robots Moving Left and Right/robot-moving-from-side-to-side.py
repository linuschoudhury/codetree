n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
time=max(sum(t),sum(t_b))
remA=t[0]
remB=t_b[0]
posA,posB=0,0
i=j=0
count=0
for _ in range(time):
    prevA,prevB=posA,posB
    if i<n:
        if d[i]=='L':
            posA-=1
        else:
            posA+=1
        remA-=1
        if remA==0:
            i+=1
            if i<n:
                remA=t[i]
    if j<m:
        if d_b[j]=='L':
            posB-=1
        else:
            posB+=1
        remB-=1
        if remB==0:
            j+=1
            if j<m:
                remB=t_b[j]
    
    if prevA!=prevB and posA==posB:
        count+=1
print(count)