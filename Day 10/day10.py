from inputday10 import *
from time import sleep
import re
"""position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>""".split('\n')
getAllInts = lambda s: map(int, re.findall(r'-?\d+', s))
y = list(map(lambda s: list(map(int, re.findall(r'-?\d+', s))), x))


def part1(inp):

    #print(lines)
    m = None
    
    for i in range(20000):
        minX = None
        for each in inp:
            if minX == None or minX> each[0]+i*each[2]:
                minX = each[0]+i*each[2]
        maxX = 0
        for each in inp:
            if maxX > each[0]+i*each[2]:
                maxX = each[0]+i*each[2]

        minY = None
        for each in inp:
            if minY == None or minY > each[1] + i * each[3]:
                minY = each[1] + i * each[3]

        maxY = 0
        for each in inp:
            if maxY > each[1]+i*each[3]:
                maxY = each[1]+i*each[3]

        xspread = maxX - minX
        yspread = maxY- minY
        
        if m==None or  m> xspread+yspread:
            m = xspread+yspread
            second=i

    grid = [['.'] * 300 for j in range(450)]
    for each in inp:
        
        x,y = each[0],each[1]
        velX = each[2]
        velY = each[3]
        #print(y + 10558 * velY, x + 10558 * velY - 250)
        grid[y + (second * velY)][x + (second * velX) - 250] = '#'

    for line in grid:
        print(''.join(line))


if __name__=="__main__":
    part1(y)
