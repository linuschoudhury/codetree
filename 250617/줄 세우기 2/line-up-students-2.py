n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
sorted_students=sorted(students,key=lambda x:(x[0],-x[1]))
for item in sorted_students:
    print(item[0],item[1],item[2])
