n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here. 
class Detail:
    def __init__(self,name,street_address,region):
        self.name=name
        self.street_address=street_address
        self.region=region
    def __str__(self):
        return f"{self.name},{self.street_address},{self.region}"
details=[]
for i in range(n):
    details_obj=Detail(name[i],street_address[i],region[i])
    details.append(details_obj)
sorted_details=sorted(details,key=lambda x:x.name)
print('name', sorted_details[-1].name)
print('addr', sorted_details[-1].street_address)
print('city', sorted_details[-1].region)