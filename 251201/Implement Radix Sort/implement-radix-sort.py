n = int(input())
arr = list(map(int, input().split()))

# Find the maximum number to determine how many digits to process
max_num = max(arr)
max_digits = len(str(max_num))

# Process from least significant to most significant digit (LSD Radix Sort)
for pos in range(max_digits):
    arr_new = [[] for _ in range(10)]
    
    for i in range(len(arr)):
        digit = (arr[i] // (10**pos)) % 10
        arr_new[digit].append(arr[i])
    
    # Update arr after processing each digit position
    arr = []
    for i in range(10):
        for j in range(len(arr_new[i])):
            arr.append(arr_new[i][j])

for num in arr:
    print(num, end=' ')