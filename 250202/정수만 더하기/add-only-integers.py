word=input()
arr=[]
for char in word:
    if '1'<=char<='9':
        arr.append(int(char))
print(sum(arr))


