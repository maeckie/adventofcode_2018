import time
test_input = 'dabAcCaCBAcCcaDA'
with open('/Users/marcus/Documents/advent/adventofcode_2018/day_5/input.txt') as file:
    for line in file:
        input = line
#input = test_input


def diffChars(a,b):
    if a.isupper() and b.islower():
        return a.lower() == b
    elif b.isupper() and a.islower():
        return b.lower() == a
    return False

def removeChars(pos):
    global input
    first_part = input[:pos]
    last_part = input[pos+2:]
    return first_part + last_part

def react():
    global input
    i = 0
    while i < len(input)-1:
        if diffChars(input[i], input[i+1]):
            input = removeChars(i)
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1 
    
def part1():
    global input
    react()
    print len(input)


def part2():
    global input
    #original = input
    polyChars = "abcdefghijklmnopqrstuvwxyz"
    mostEffective = 100000
    react()
    original = input
    for p in polyChars:
        input = input.replace(p,'').replace(p.upper(),'')
        react()
        if mostEffective > len(input):
            mostEffective = len(input)
        input = original
    print mostEffective
    


#start_time = time.time()
#part1()
#print("Execution on part 1:  %s seconds ---" % (time.time() - start_time))

#start_time = time.time()
#part2()
#print("Execution on part 2:  %s seconds ---" % (time.time() - start_time))
res = input[0]
#print test_input[-1:]
for i in range(1, len(input)):
    if abs(ord(input[i]) - ord(res[-1:])) != 32:
        res = res + input[i]
    else:
        res = res[:-1]
    
print res
#print [res + = test_input[i]) for i in range(0, len(test_input)-1) if (abs(ord(test_input[i]) - ord(test_input[i+1])) != 32) and (abs(ord(test_input[i]) - ord(res[-1:])) != 32)]
