n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!
def addarray():
    for i in range(len(queries)):
        total=0
        for j in range (queries[i][0]-1,queries[i][1]):
            total+=arr[j]
        print(total)
addarray()
    
