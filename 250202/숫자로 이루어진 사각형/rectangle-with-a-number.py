n = int(input())

# Write your code here!

def printthis(side):
    count=1
    for i in range(side):
        for j in range(side):
            if count%10==0:
                count+=1
            print(count%10,end=' ')
            count+=1
        print()
printthis(n)