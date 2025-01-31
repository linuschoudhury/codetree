input_str = input()
target_str = input()

# Write your code here!
matched=-1
pos=-1
for i in range(len(input_str)):

    if input_str[i]==target_str[0]:
        matched=1
        
        for j in range(len(target_str)):
            if input_str[i+j]!=target_str[j]:
                matched=-1
                #print(1)
                break
        if matched==1:
            pos=i
            break
        

print(pos)
