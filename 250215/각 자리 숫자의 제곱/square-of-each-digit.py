N = int(input())

# Write your code here!
def squaresums(n):
    if n==0:
        return 0
    return squaresums(n//10)+((n%10)*(n%10))
print(squaresums(N))