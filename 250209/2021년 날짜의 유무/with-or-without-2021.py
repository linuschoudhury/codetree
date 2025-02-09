M, D = map(int, input().split())

# Write your code here!
def dateExists(M,D):
    if M in [1,3,5,7,8,10,12]:
        if 1<=D<=31:
            return 'Yes'
    elif M in [4,6,9,11]:
        if 1<=D<=30:
            return 'Yes'
    elif M==2:
        if 1<=D<=28:
            return 'Yes'
    return 'No'

print(dateExists(M,D))
    