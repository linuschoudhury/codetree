a, b, c = map(int, input().split())

# Write your code here!
def func(prod,total=0):
    if prod==0:
        return total
    
    return func(prod//10,total+prod%10)

print(func(a*b*c))

