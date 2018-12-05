#!/usr/bin/python
import re
import collections
import datetime
import time


with open('/Users/marcus/Documents/advent/adventofcode_2018/day_4/gute_input.txt') as file:
    input = file.readlines()

input = map(lambda x: x.replace('\n', ''), input)

d = {}
for line in input:
    m = re.match('\[(.*)\](.*)', line)
    d[m.group(1)] = m.group(2)



def break_down_guard_sleep():
    all_guards = {}
    guard = 0
    for key in sorted(d):
        if 'Guard' in d[key]:
            guard = re.search('Guard #(\d+) begins shift', d[key]).group(1)
            if guard not in all_guards:
                all_guards[guard] = {'total':0, 'all_mins': []}
        elif 'sleep' in d[key]:
            start_sleep  = int(key.split(':')[1])

        else:
            stop_sleep  = int(key.split(':')[1])
            mins = stop_sleep - start_sleep
            all_guards[guard]['total'] += mins
            #start_min = int(str(start_sleep).split(':')[1])
            all_guards[guard]['all_mins'].extend(range(start_sleep,mins+start_sleep))
    return all_guards

def part1():
    all_guards = break_down_guard_sleep()
    find_max = ''
    for itm in all_guards:
        if find_max == '':
            find_max = itm
        elif all_guards[itm]['total'] > all_guards[find_max]['total']:
            find_max = itm

    print int(find_max) * max(set(all_guards[find_max]['all_mins']), key=all_guards[find_max]['all_mins'].count)

def part2():
    all_guards = break_down_guard_sleep()
    find_max = 0
    g = 0
    minute = 0
    for guard in all_guards:
        mins = collections.Counter(all_guards[guard]['all_mins'])
        for m in mins.most_common():
            if m[1] > find_max:
                minute = m[0]
                find_max = m[1]
                g = guard
            break
            
    print int(g) * int(minute)
        


part1()
part2()
