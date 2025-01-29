n, m = map(int, input().split())

# Write your code here!
matrix = [[0] * m for _ in range(n)]
curr = 1
for diagonal in range(n + m - 1):
    start_row = max(0, diagonal - m + 1)
    start_col = min(diagonal, m - 1)
    
    i, j = start_row, start_col
    while i < n and j >= 0:
        matrix[i][j] = curr
        curr += 1
        i += 1
        j -= 1
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=' ')
    print()
