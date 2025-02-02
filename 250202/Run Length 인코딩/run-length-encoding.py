A = input()
string=''

# Write your code here!
i=0
while i<len(A):
    currentcount=1
    for j in range(i+1,len(A)):
        if A[i]==A[j]:
            currentcount+=1
        else:
            break
    string=string+A[i]+str(currentcount)
    i+=currentcount
print(len(string))
print(string)
    
            

        


