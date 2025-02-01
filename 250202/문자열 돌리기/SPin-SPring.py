s=input()
print(s)
for i in range(len(s)):
    s=s[-1]+s[:len(s)-1]
    print(s)