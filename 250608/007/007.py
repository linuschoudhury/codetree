secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Ramen:
    def __init__(self,secret_code,meeting_point,time):
        self.secret_code=secret_code
        self.meeting_point=meeting_point
        self.time=time
ramen1=Ramen(secret_code,meeting_point,time)
print("secret code :",ramen1.secret_code)
print("meeting point :",ramen1.meeting_point)
print("time :",ramen1.time)