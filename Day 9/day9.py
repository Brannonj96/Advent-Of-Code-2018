from inputday9 import *
import re
from collections import deque, defaultdict


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
class doubleEndedQ:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count=0


    def __str__(self):
        s=''
        cur = self.head
        while cur!=None:
            s+= ((str(cur.data)) + ' ')
            cur = cur.right
        return s

    def push(self,data):
        if self.head == None:
            self.head = self.tail = Node(data)
        elif self.head==self.tail:
            self.head = Node(data, None, self.tail)
            self.tail.left = self.head
        else:
            self.head = Node(data,None, self.head)
            self.head.right.left = self.head
        self.count +=1

    def append(self, data):
        if self.tail == None:
            self.tail = self.head = Node(data)
        elif self.head == self.tail:
            self.tail = Node(data, self.head, None)
            self.head.right = self.tail
        else:
            self.tail = Node(data, self.tail, None)
            self.tail.left.right = self.tail
        self.count+=1

    def pop(self):
        #print(self.head, self.tail)
        data = None
        if self.head==self.tail:
            data = self.head.data
            self.head = self.tail = None
            self.count = 0
        elif self.head!=None:
            data = self.head.data
            self.head = self.head.right
            self.head.left = None
            self.count-=1
        #print(self.head, self.tail)
        return data

        
        
    def removeBack(self):
        data = None
        if self.tail == self.head:
            data = self.tail.data
            self.tail = self.head = None
            self.count=0
        elif self.tail!=None:
            data = self.tail.data
            self.tail = self.tail.left
            self.tail.right = None
            self.count-=1
        return data
        

def part1(last, numPlay):
    circle = [0]
    current = 0
    players = {i:0 for i in range(numPlay)}
    for i in range(1,last+2):
        if i%10000==0:
            print(i)
        #print(current, circle[current])
        #print(circle)
        if i%23!=0:
            l = len(circle)
            one_clock = (current+1)%l
            circle.insert(one_clock+1, i)
            current = (one_clock+1)
            #print(circle)
        else:
            pointsIndex = (current-7)%len(circle)
            players[i%numPlay]+= circle[pointsIndex]
            #print("Adding",circle[pointsIndex])
            players[i%(numPlay)] += i
            #print("Adding",i)
            del circle[pointsIndex]
            current = pointsIndex


    m = 0
    for k,v in players.items():
        if v>m:
            m=v
            i = k
    #print(players)
    print(m)
            
        
    

def part2(last, numPlay):
    circle = doubleEndedQ()
    circle.push(0)
    players = {i:0 for i in range(numPlay)}
    for i in range(1,last+2):
        if i%10000==0:
            print(i)
        #print(current, circle[current])
        #print(circle)
        if i%23!=0:
            for j in range(2):
                circle.append(circle.pop())
            circle.push(i)
            #print(circle)
        else:
            for j in range(6):
                circle.push(circle.removeBack())

            players[i%numPlay] += (i+circle.removeBack())

            


    m = 0
    for k,v in players.items():
        if v>m:
            m=v
            i = k
    #print(players)
    print(m)

def main(inp):

    part1(70723, 427)

    part2(7072300, 427)


if __name__=="__main__":
    
    main(x)

