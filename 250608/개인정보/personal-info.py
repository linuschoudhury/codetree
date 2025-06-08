n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
individuals=[]
for i in range(5):
    ind_obj=(name[i],height[i],weight[i])
    individuals.append(ind_obj)
individuals.sort(key=lambda x:(x[0],-x[1]))
print('name')
for i in range(5):
    print(individuals[i][0],individuals[i][1],individuals[i][2])
individuals.sort(key=lambda x:(-x[1],x[0]))
print()
print('height')
for i in range(5):
    print(individuals[i][0],individuals[i][1],individuals[i][2])