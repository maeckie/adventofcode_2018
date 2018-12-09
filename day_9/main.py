#441 players; last marble is worth 71032 points
players = 441
last_marble_worth = 71032
circle = [0]
curr = 0

score = {}
i = 1
p = 1
while i <= last_marble_worth:
    if i % 100000 == 0:
        print i
    if i % 23 == 0:
        if p not in score:
            score[p] = 0
        score[p] += i 
        remove = curr - 7
        curr = remove
        if remove < 0 :
            remove = len(circle) + remove
        curr = remove
        score[p] += circle[remove]
        del(circle[remove])
    else:
        insert_at = curr + 2
        if insert_at > len(circle):
            insert_at = insert_at - len(circle)
        circle.insert(insert_at, i)    
        curr = insert_at
    p+=1
    if p > players:
        p = 1    
    i+= 1

print max(score.values())