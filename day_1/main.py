#!/usr/bin/python
import sys

with open('/Users/marcus/Documents/advent/adventofcode_2018/day_1/input.txt') as file:
    freq_changes = file.readlines()

def part1():
    global freq_changes
    frequence_sum = reduce((lambda x,y: x+y), freq_changes)
    print "The resulting frequence is: %d" % frequence_sum

def part2():
    global freq_changes
    freq_sum = 0
    all_sums = {}
    all_sums[freq_sum] = 0
    while True:
        for i in freq_changes:
            freq_sum += i
            if freq_sum in all_sums:
                print "The first one to appear twice is: %d" % freq_sum
                sys.exit(1)
            all_sums[freq_sum] = 0

# Remove newlines and covert to ints.
freq_changes = map(lambda x: int(x.replace('\n', '')), freq_changes)

part1()
part2()
