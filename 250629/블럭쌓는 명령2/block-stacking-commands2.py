n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

array=[0]*n

for i in range(k):
    for j in range(commands[i][0]-1,commands[i][1]):
        array[j]+=1
        #print(j)

    #array[commands[i][1]]+=1


print(max(array))
