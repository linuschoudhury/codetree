MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Score:
    def __init__(self,codename,score): 
        self.codename=codename
        self.score=score
smallestindex=0
for i in range(5):
    if scores[i]<scores[smallestindex]:
        smallestindex=i

score1=Score(codenames[smallestindex],scores[smallestindex])
print(score1.codename, score1.score)