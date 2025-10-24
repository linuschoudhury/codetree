board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
seq1='11111'
seq2='22222'
found=False
for i,row in enumerate(board):
    rowstring=''.join(map(str,row))
    if seq1 in rowstring:
        print(1)
        print(i+1,rowstring.index(seq1)+3)
        found=True
        break
    if seq2 in rowstring:
        print(2)
        print(i+1,rowstring.index(seq2)+3)
        found=True
        break
for col in range(19):
    colstring=''.join(str(board[row][col]) for row in range(19))
    if seq1 in colstring:
        print(1)
        print(colstring.index(seq1)+3,col+1)
        found=True
        break
    if seq1 in colstring:
        print(2)
        print(colstring.index(seq2)+3,col+1)
        found=True
        break