
import re
from copy import deepcopy

states = """.#.## => .
.#### => .
#..#. => .
##.## => #
..##. => #
##... => #
..#.. => #
#.##. => .
##.#. => .
.###. => #
.#.#. => #
#..## => #
.##.# => #
#.### => #
.##.. => #
###.# => .
#.#.# => #
#.... => .
#...# => .
.#... => #
##..# => .
....# => .
..... => .
.#..# => #
##### => .
#.#.. => .
..#.# => #
...## => .
...#. => #
..### => .
####. => #
###.. => #""".split('\n')

states = {each.split(' => ')[0]:each.split(' => ')[1] for each in states}

#print(states)

#x = '......................................................................#......##...#.#.###.#.##..##.#.....##....#.#.##.##.#..#.##........####.###.###.##..#....#...###.##.............................................................'
x = (['.']*101)+list('###......#.#........##.###.####......#..#####.####..#.###..#.###.#..#..#.#..#..#.##...#..##......#.#') + (['.']*100)
def part1(inp):
    #inp = '..............#..#.#..##......###...###......................'
    initial = inp.index('#')
    last = sum([i-initial for i in range(len(inp)) if inp[i]=='#'])
    f=0
    prev = 0
    for i in range(500):
        replace = inp+[]
        for j in range(2,len(inp)-2):
            group = inp[j-2]+inp[j-1]+inp[j]+inp[j+1]+inp[j+2]
            if group in states:
                replace[j] = states[group]
            else:
                replace[j] = '.'
        inp = replace
        #print(inp[:15])
        if '#' in inp[:10] or '#' in inp[-10:]:
            inp = (['.']*100) + inp + (['.']*100)
            initial+=100
        #print(inp)

        
        #print(len(inp))
        mid = len(inp)/2 -.5
        
        nxt= sum([i-initial for i in range(len(inp)) if inp[i]=='#'])

        
        cur = nxt-last

        #print(cur)
        prev = cur
        last = nxt
    print(last)
    print(last+(50000000000-500)*prev)
    
        

        
def part2(inp):
    pass


def main(inp):
    part1(inp)
    part2(inp)


if __name__=="__main__":
    main(x)
