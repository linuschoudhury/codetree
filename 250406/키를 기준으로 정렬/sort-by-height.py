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
class Stats:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
stats=[]
for i in range(n):
    stats.append(Stats(name[i],height[i],weight[i]))
stats.sort(key=lambda x: x.height)
for i in range(n):
    print(stats[i].name,stats[i].height,stats[i].weight)