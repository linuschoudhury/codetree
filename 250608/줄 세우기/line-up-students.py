n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]


    
for student in students:
    students.sort(key=lambda x:(-x[0],-x[1],-x[2]))
for student in students:
    print(student[0], student[1], student[2])

