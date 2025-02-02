n = int(input())

# Write your code here!
def by5(a):
    result=''
    digitsum=(a//10)+(a%10)
    if n%2==0 and digitsum%5==0:
        result='Yes'
    else:
        result='No'
    return result
print(by5(n))
    
