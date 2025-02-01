A=input()
command=input()

# Write your code here!
for i in range(len(command)):
    if command[i]=='L':
        A=A[1:len(A)]+A[0]
    elif command[i]=='R':
        A=A[-1]+A[0:len(A)-1]
print(A)