board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.

found = False

for i in range(19):
    for j in range(19):
        if board[i][j] == 0:
            continue
        
        player = board[i][j]
        
        if i+4 < 19:
            count = 0
            for k in range(5):
                if board[i+k][j] == player:
                    count += 1
                else:
                    break
            if count == 5:
                print(player)
                print(i+3, j+1)
                found = True
                break
        
        if not found and j+4 < 19:
            count = 0
            for k in range(5):
                if board[i][j+k] == player:
                    count += 1
                else:
                    break
            if count == 5:
                print(player)
                print(i+1, j+3)
                found = True
                break
        
        # Diagonal down-right
        if not found and i+4 < 19 and j+4 < 19:
            count = 0
            for k in range(5):
                if board[i+k][j+k] == player:
                    count += 1
                else:
                    break
            if count == 5:
                print(player)
                print(i+3, j+3)
                found = True
                break
        
        if not found and i+4 < 19 and j-4 >= 0:
            count = 0
            for k in range(5):
                if board[i+k][j-k] == player:
                    count += 1
                else:
                    break
            if count == 5:
                print(player)
                print(i+3, j-1)
                found = True
                break
    
    if found:
        break

if not found:
    print(0)
