y = int(input())

# Write your code here!
def isleap(a):
    result='true'
    if a%4!=0:
        result= 'false'
    if a%100==0:
        if a%400!=0:
            result= 'false'
    return result
print(isleap(y))
