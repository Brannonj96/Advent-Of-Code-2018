from inputday7 import *
from collections import OrderedDict


"""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""".split('\n')
req = {}
avail = []
unlocks = {}
f = True
for each in x:
    first, nxt = each[5], each[36]
    if nxt not in req:
        req[nxt] = []
    if first not in unlocks:
        unlocks[first] = []
    req[nxt].append(first)
    unlocks[first].append(nxt)

for each in unlocks:
    if each not in req:
        avail.append(each)
done = ''
#print('Unlocks',unlocks)
#print('Requires', req)
#print(['F'])
#print(req['Z'])

alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

w = [[None,0],[None,0],[None,0],[None,0],[None,0]]

s=0
f=True
while f:
    avail=sorted(avail)
    for i in range(min(5, len(avail))):
        if w[0][0]==None:
            w[0][0] = avail[0]
            w[0][1] = (61 + alp.index(w[0][0]))
            del avail[0]
            continue
        if w[1][0]==None:
            w[1][0] = avail[0]
            w[1][1] = (61 + alp.index(w[1][0]))
            del avail[0]
            continue
        
        if w[2][0]==None:
            w[2][0] = avail[0]
            w[2][1] = (61 + alp.index(w[2][0]))
            del avail[0]
            continue
        if w[3][0]==None:
            w[3][0] = avail[0]
            w[3][1] = (61 + alp.index(w[3][0]))
            del avail[0]
            continue
        if w[4][0]==None:
            w[4][0] = avail[0]
            w[4][1] = (61 + alp.index(w[4][0]))
            del avail[0]
            continue
        
    #q = str(s)+' '+str(w)
    #print(y[s],'\n',q)
    #if q != y[s]:
        #print(q)
    #else:
    #    print('True')
            
    for ws in w:
        if ws[0]==None:
            continue
        
        ws[1]-=1
        if ws[1]<=0:
            done+= ws[0]
            if ws[0] not in unlocks:
                f=False
                break
            for each in unlocks[ws[0]]:
            #print(each, req[each])
                for otherEach in req[each]:
                    if otherEach not in done:
                        break
                else:
                    avail.append(each)
            ws[0] = None
            ws[1] = 0
        #print(order)
    s+=1

print(done,s)

