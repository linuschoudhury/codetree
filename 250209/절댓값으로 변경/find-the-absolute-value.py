n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
def absolute(array):
    for elem in array:
        elem=abs(elem)
        print(elem,end=' ')
absolute(arr)