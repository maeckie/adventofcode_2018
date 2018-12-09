from collections import deque
players = 441
last_marble = 71032 * 100
#players = 10
#last_marble = 25
circle = deque([0])
p = 1
score = {}

for i in range(1,last_marble+1):
    if i % 23 == 0:
        if p not in score:
            score[p] = 0
        circle.rotate(7)
        score[p] += i + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(i)
    p += 1
    if p > players:
        p = 1
    #print circle
print max(score.values())
