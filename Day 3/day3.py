from inputday3 import *

seenCords = dict()
uids = set()
sqin = 0
for each in x:
    line = each.split()
    id = line[0]
    uids.add(id)
    left,top = map(int,line[2][:-1].split(','))
    #print(line)
    left+=1
    top+=1
    #print(left,right)
    w,h = map(int,line[3].split('x'))
    for row in range(h):
        for column in range(w):
            point = (left+column, top+row)
            #print(point,'point\n\n')
            if point in seenCords:
                seenCords[point][1].add(id)
                for eachId in seenCords[point][1]:
                    if eachId in uids:
                        uids.remove(eachId)
                if seenCords[point][0] == 0:
                    sqin+=1
                    seenCords[point][0]+=1
            else:
                seenCords[point] = [0, set([id])]


print(sqin)
print(uids)

