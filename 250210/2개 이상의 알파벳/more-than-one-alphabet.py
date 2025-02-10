A = input()

# Write your code here!
def this(string):
    for i in range(len(string)-1):
        if string[i+1]!=string[i]:
            return 'Yes'
    return 'No'
print(this(A))
