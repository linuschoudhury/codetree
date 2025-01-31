word=input()
word=word[:1]+'a'+word[2:]
word=word[:len(word)-2]+'a'+word[len(word)-1:]
print(word)