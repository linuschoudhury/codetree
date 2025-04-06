n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class Student:
    def __init__(self,name,korean,english,math):
        self.name=name
        self.korean=korean
        self.english=english
        self.math=math
students=[]

for i in range(n):
    student_obj=Student(name[i],korean[i],english[i],math[i])
    students.append(student_obj)
students.sort(key=lambda x:(-x.korean,-x.english,-x.math))
#print(students)
for i in range(n):
#    print(students[i].name)
    print(students[i].name,students[i].korean,students[i].english,students[i].math)
