try:
    word = input()
    while len(word) > 0:
        word = list(word)
        try:
            pos = int(input())
            if pos < len(word):
                word.pop(pos)
            else:
                word.pop(len(word)-1)
            word = ''.join(word)
            print(word)
        except EOFError:
            break
except EOFError:
    pass

    