Y, M, D = map(int, input().split())

# Write your code here!
def season(y,m,d):
    if m in [3,4,5]:
        return 'Spring'
    elif m in [6,7,8]:
        return 'Summer'
    elif m in [9,10,11]:
        return 'Fall'
    elif m in [1,2,12]:
        return 'Winter'
    else:
        return -1

def dateExists(y,m,d):
    if m in [1,3,5,7,8,10,12]:
        if 1<=d<=31:
            return 'Yes'
    elif m in [4,6,9,11]:
        if 1<=d<=30:
            return 'Yes'
    elif m==2 and y%4!=0:
        if 1<=d<=28:
            return 'Yes'
    elif m==2 and y%4==0:
        if y%100!=0:
            if 1<=d<=29:
                return 'Yes'
        elif y%100==0 and y%400==0:
            if 1<=d<=29:
                return 'Yes'
    return -1

if dateExists(Y,M,D) == -1:
    print(dateExists(Y,M,D))
else:
    print(season(Y,M,D))
    
