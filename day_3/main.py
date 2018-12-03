#!/usr/bin/python
import re

with open('/Users/marcus/Documents/advent/adventofcode_2018/day_3/input.txt') as file:
    input = file.readlines()

def part1():
    w, h = 2000, 2000;
    matrix = [[0 for x in range(w)] for y in range(h)]
    overlaps = 0
    intact= {}
    for i in input:
        m = re.search('.*#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+).*', i)
        id = m.group(1)
        margin_left = int(m.group(2))
        margin_top = int(m.group(3))
        width = int(m.group(4))
        height = int(m.group(5))
        for y in range(margin_top, margin_top+height):
            for x in range(margin_left, margin_left+width):
                if matrix[y][x] != 0:
                    if matrix[y][x] != 'x':
                        matrix[y][x] = 'x'
                        overlaps += 1
                else:
                    matrix[y][x] = id


    print overlaps

def part2():
    w, h = 2000, 2000;
    matrix = [[0 for x in range(w)] for y in range(h)]
    overlaps = 0
    intact= {}
    for i in input:
        m = re.search('.*#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+).*', i)
        id = m.group(1)
        margin_left = int(m.group(2))
        margin_top = int(m.group(3))
        width = int(m.group(4))
        height = int(m.group(5))
        bool_intact = True
        to_remove = []
        for y in range(margin_top, margin_top+height):
            for x in range(margin_left, margin_left+width):
                if matrix[y][x] != 0:
                    to_remove.append(matrix[y][x])
                    matrix[y][x] = id
                    bool_intact = False
                else:
                    matrix[y][x] = id


        if bool_intact:
            intact[id] = None

        for itm in to_remove:
            if itm in intact:
                intact.pop(itm)

    print intact

part2()
