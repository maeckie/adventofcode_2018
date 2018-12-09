

import re
import sys

def findRoot(graph):
    parents = []
    children = []
    for itm in graph:
        parents.extend(itm)
        children.extend(graph[itm])
    return list(set(parents) - set(children))

def findParents(child, graph):
    parents = []
    for itm in graph:
        if child in graph[itm]:
            parents.extend(itm)
    return parents

def checkParentsVisited(child, graph):
    parents = findParents(child, graph)
    if len(parents) > 0:
        return False
    return True

def part1(graph):
    
    candidates = findRoot(graph)
    candidates.sort()

    i = 0
    res = ""
    while len(candidates) > 0:
        candidates = list(set(candidates))
        candidates.sort()
        cand = candidates[i]

        if checkParentsVisited(cand, graph):
            if cand in graph:
                candidates.extend(graph[cand])

            if cand in graph:
                graph.pop(cand)
            res += cand
            del(candidates[i])
            i = 0
        else:
            i += 1
                
    print res



def getFreeWorker(workers, cand):
    if len(workers) < 4:
        for w in workers:
            if w[0] == cand:
                return False
        return True
    return False

def part2(graph):
    workers = []
    candidates = findRoot(graph)
    candidates.sort()

    i = 0
    res = ""
    s = 0
    while len(candidates) > 0:
        candidates = list(set(candidates))
        candidates.sort()
        for worker in workers:
            if worker[1] == s:
                cand = worker[0]
                if cand in graph:
                    candidates.extend(graph[cand])

                if cand in graph:
                    graph.pop(cand)
                res += cand
                candidates.remove(cand)
                workers.remove(worker)
        
        for cand in candidates:
            if checkParentsVisited(cand, graph):
                if getFreeWorker(workers, cand):
                    workers.append((cand, s + ord(cand)-4))
        print workers
        s += 1
    print s-1
    print res

    
    
    


        


graph = {}
with open('/Users/marcus/Documents/advent/adventofcode_2018/day_7/input.txt') as file:
    for line in file:
        m = re.search('Step (\w) must be finished before step (\w) can begin.', line)
        parent = m.group(1)
        child = m.group(2)
        if parent not in graph:
            graph[parent] = []    
        graph[parent].append(child)




part2(graph)
#print findRoot(graph)
#print findParents(graph, 'E')
#part1(graph)
