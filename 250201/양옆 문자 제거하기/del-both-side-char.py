word=input()
word=list(word)
word.pop(1)
word.pop(len(word)-2)
print(''.join(word))

