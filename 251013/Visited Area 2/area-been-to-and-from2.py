n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
arr=[]
offset=50
cur=0
segments=[]
for i in range(n):
    if dir[i]=='L':
        section_left=cur-x[i]
        section_right=cur
        cur-=x[i]
    else:
        section_left=cur
        section_right=cur+x[i]
        cur+=x[i]
    segments.append([section_left,section_right])


for segment in segments:
    for j in range(segment[0],segment[1]):
        arr.append(j)

freq_dict={}
for num in arr:
    if num in freq_dict:
        freq_dict[num]+=1
    else:
        freq_dict[num]=1

count=0
for num in freq_dict:
    if freq_dict[num]>=2:
        count+=1
print(count)


