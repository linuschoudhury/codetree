arr=["apple","banana","grape","blueberry","orange"]
char=input()
result=[]

for i in range(len(arr)):
    flag=False
    if arr[i][2]==char or arr[i][3]==char:
        result.append(i)
for i in range(len(result)):
    print(arr[result[i]])
print(len(result))

        


