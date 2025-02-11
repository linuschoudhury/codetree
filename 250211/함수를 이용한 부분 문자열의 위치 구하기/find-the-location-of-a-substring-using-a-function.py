text = input()
pattern = input()

# Write your code here!
sub=False

def findpos():
    pos=-1
    for i in range(len(text)):
        if text[i]==pattern[0] and i+len(pattern)<=len(text):
            sub=True
            pos=i
            for j in range(len(pattern)):
                if pattern[j]!=text[i+j]:
                    sub=False
                    break
    return pos
print(findpos())
        