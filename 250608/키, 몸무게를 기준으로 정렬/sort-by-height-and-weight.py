n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
individuals=[]
for i in range(n):
    ind_obj=(name[i],height[i],weight[i])
    individuals.append(ind_obj)
individuals.sort(key=lambda x:(x[1],-x[2]))
for i in range(n):
    print(individuals[i][0],individuals[i][1],individuals[i][2])
