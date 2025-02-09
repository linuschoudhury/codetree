A = input()

# Write your code here!
def palindrome(string):
    if list(string)==list(string[::-1]):
        print('Yes')
    else:
        print('No')
palindrome(A)
