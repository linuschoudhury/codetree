n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

tiles = {}   # pos -> {'w': count, 'b': count, 'last': 'W' or 'B'}
curr = 0     # current position

for num, direction in commands:
    steps = int(num)
    if direction == 'R':
        step = 1
        color = 'B'
    else:  # 'L'
        step = -1
        color = 'W'

    for k in range(steps):
        # paint current tile
        if curr not in tiles:
            tiles[curr] = {'w': 0, 'b': 0, 'last': None}
        if direction == 'L':
            tiles[curr]['w'] += 1
        else:
            tiles[curr]['b'] += 1
        tiles[curr]['last'] = color

        # move, except after the last paint
        if k != steps - 1:
            curr += step

# Count results
white = black = gray = 0
for t in tiles.values():
    if t['w'] >= 2 and t['b'] >= 2:
        gray += 1
    elif t['last'] == 'W':
        white += 1
    else:
        black += 1

print(white, black, gray)
