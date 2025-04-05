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
score1=Score(codenames[0],scores[0])
print(score1.codename, score1.score)