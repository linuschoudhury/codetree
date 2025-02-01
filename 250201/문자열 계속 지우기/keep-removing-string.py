A = input()
B = input()
pos=-1
# Write your code here!
while True:
    matched=-1
    pos=-1
    for i in range(len(A)):
        if i+len(B)<=len(A):
            if A[i]==B[0]:
                matched=1
                
                for j in range(len(B)):
                    if A[i+j]!=B[j]:
                        matched=-1
                        #print(1)
                        break
                if matched==1:
                    pos=i
                    break
    if pos==-1:
        break
    A=A[:pos]+A[pos+len(B):]
print(A)