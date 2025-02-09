n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
def modify(array):
    for elem in array:
        if elem%2==0:
            elem=elem//2
        print(elem,end=' ')
modify(arr[:])