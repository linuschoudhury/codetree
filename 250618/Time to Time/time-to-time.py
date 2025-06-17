a, b, c, d = map(int, input().split())

# Please write your code here.
if d>=c:
    minresult=d-b
    hourresult=c-a
else:
    minresult=(d-b)+60
    hourresult=(c-a)-1
totalmin=(hourresult*60)+minresult
print(totalmin)
