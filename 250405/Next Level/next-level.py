user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Lmao:
    def __init__(self,user2_id,user2_level):
        self.user2_id=user2_id
        self.user2_level=user2_level
lmao=Lmao(user2_id,user2_level)
print('user codetree lv 10')
print('user',user2_id,end=' ')
print('lv', user2_level)
