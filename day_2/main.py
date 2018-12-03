#!/usr/bin/python
from collections import Counter
from itertools import combinations
import time


checksum_input = {2:0, 3:0}
with open('/Users/marcus/Documents/advent/adventofcode_2018/day_2/input.txt') as file:
    boxes = file.readlines()
boxes = map(lambda x: x.replace('\n', ''), boxes)

boxes = ['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']

def part1():
    global boxes
    for box in boxes:
        occurrances = Counter(box)
        if any(v == 2 for v in occurrances.itervalues()):
            checksum_input[2] += 1
        if any(v == 3 for v in occurrances.itervalues()):
            checksum_input[3] += 1

    print "The checksum is: %d" % (checksum_input[2] * checksum_input[3])


def part2():
    start = 1
    for box in boxes:
        i = start
        while i < len(boxes):
            comp = boxes[i]
            diff = 0
            j = 0
            result = ''
            while j < len(box):
                if box[j] != comp[j]:
                    diff += 1
                else:
                    result += box[j]
                j += 1
            if diff == 1:
                print "The common letters are: %s " % result
            i += 1
        start += 1

start_time = time.time()
part1()
print("Execution on part 1:  %s seconds ---" % (time.time() - start_time))
part2()
start_time = time.time()
print("Execution on part 2:  %s seconds ---" % (time.time() - start_time))
