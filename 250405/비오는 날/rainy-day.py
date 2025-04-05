n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class Stats:
    def __init__(self,date,day,weather):
        self.date=date
        self.day=day
        self.weather=weather
    def __str__(self):
        return f"{self.date},{self.day},{self.weather}"
stats=[]
for i in range(n):
    stats_obj=Stats(date[i],day[i],weather[i])
    stats.append(stats_obj)
sorted_stats=sorted(stats,key=lambda x:x.date)
for i in range(n):
    if sorted_stats[i].weather=='Rain':
        print(sorted_stats[i].date,sorted_stats[i].day,sorted_stats[i].weather)
        break

