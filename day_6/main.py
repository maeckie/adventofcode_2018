coordinates = []
import re
#from operator import itemgetter
import time

with open('/Users/marcus/Documents/advent/adventofcode_2018/day_6/input.txt') as file:
    for line in file:
        m = re.search('(\d+),\s(\d+)', line)
        coordinates.append((int(m.group(1)), int(m.group(2))))
    
inf_cand = []
def find_max_min(coords):
    x_max = 0
    x_min = 500
    y_min = 500
    y_max = 0
    for c in coords:
        if c[0] > x_max: x_max = c[0] 
        if c[0] < x_min: x_min = c[0] 
        if c[1] > y_max: y_max = c[1]
        if c[1] < y_min: y_min = c[1]
    return ((x_min,x_max), (y_min,y_max))

def inf_candidate(x,y,start_stop):
    if x == start_stop[0][0] or x == start_stop[0][1] or y == start_stop[1][0] or y == start_stop[1][1]:
        return True
    return False

def calculate_point(x,y,coord, start_stop):
    global inf_cand
    closest = {}
    for c in coord:
        shortest = 10000000    
        distance = abs(c[0] - x) + abs(c[1] - y)
        if distance < shortest:
            shortest = distance
        closest[c] = shortest
    m = min(closest.values())
    if closest.values().count(m) > 1:
        return None
    else:
        if inf_candidate(x,y,start_stop):
            inf_cand.append(closest.keys()[closest.values().index(m)])
        return closest.keys()[closest.values().index(m)]

def part1(coords):
    global inf_cand
    start_stop = find_max_min(coordinates)   
    area_map = {}
    for x in range(start_stop[0][0], start_stop[0][1]+1):
        for y in range(start_stop[1][0], start_stop[1][1]+1):
            p = calculate_point(x,y,coords, start_stop)
            if p is not None:
                if area_map.has_key(p): 
                    area_map[p] += 1
                else:
                    area_map[p] = 1

    for itm in inf_cand:
        if area_map.has_key(itm):
            area_map.pop(itm)
    
    print max(area_map.values())        

def part2(coords):
    start_stop = find_max_min(coords)
    res = 0
    for x in range(start_stop[0][0], start_stop[0][1]+1):
        for y in range(start_stop[1][0], start_stop[1][1]+1):
            sum_c = 0
            for c in coords:
                sum_c += abs(c[0] - x) + abs(c[1] - y)
            if sum_c < 10000:
                res += 1

    print res
#part1(coordinates)
#part2(coordinates )


start_time = time.time()
part1(coordinates)
print("Execution on part 1:  %s seconds ---" % (time.time() - start_time))

start_time = time.time()
part2(coordinates)
print("Execution on part 2:  %s seconds ---" % (time.time() - start_time))
