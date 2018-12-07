from inputday7 import *
#from collections import OrderedDict hey screw this i dont need it


"""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""".split('\n')


def part1(x):
        #This will be a dictionary of what a letter needs to have done to be able
    #to run
    req = {}

    #What is currently available to run
    avail = []

    #When one letter is unlocked this runs
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

    #If something is in unlocks and not in req it is a start state
    for each in unlocks:
        if each not in req:
            avail.append(each)

    #The order
    done = ''

    #If avail has stuff in it, then go
    #an empty list is False
    while avail:
        avail=sorted(avail)
        nxt = avail[0]
        del avail[0]
        done+=nxt
        #The final state does not unlock anything so break
        if nxt not in unlocks:
            break
        #Else everything that could be unlocked by this next
        for each in unlocks[nxt]:

            #Check all the requirements for that new letter
            for otherEach in req[each]:
                #if it's not done, then break if we do not break, make it
                #a possible next step
                if otherEach not in done:
                    break
            else:
                avail.append(each)
    print(done)


def part2(x):
    #This will be a dictionary of what a letter needs to have done to be able
    #to run
    req = {}

    #What is currently available to run
    avail = []

    #When one letter is unlocked this runs
    unlocks = {}


    for each in x:
        #get the letters
        first, nxt = each[5], each[36]
        if nxt not in req:
            req[nxt] = []
        if first not in unlocks:
            unlocks[first] = []

                
        req[nxt].append(first)
        
        unlocks[first].append(nxt)

    #Same deal as up there
    for each in unlocks:
        if each not in req:
            avail.append(each)
            
    done = ''
    #print('Unlocks',unlocks)
    #print('Requires', req)
    #print(['F'])
    #print(req['Z'])

    #The index will add our time
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Got 5 workers [0] is the job and [1] is how much time till completion
    w = [[None,0],[None,0],[None,0],[None,0],[None,0]]

    #The second
    s=0
    f=True
    while f:
        avail=sorted(avail)

        #If len is shorter than 5, we use it else try to assign all 5
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
            #if it has no job, just check the next
            if ws[0]==None:
                continue
            #It has worked for one second
            ws[1]-=1
            
            if ws[1]<=0:
                #If it is 0 or less then the task is done
                done+= ws[0]

                #if the task doesn't unlock anything, set f to False
                #it is our last state
                if ws[0] not in unlocks:
                    f=False
                    break
                #Same deal as part 1
                for each in unlocks[ws[0]]:
                #print(each, req[each])
                    for otherEach in req[each]:
                        if otherEach not in done:
                            break
                    else:
                        avail.append(each)
                #Set available for job and back to 0
                ws[0] = None
                ws[1] = 0
            #print(order)
        s+=1

    print(done,s)

if __name__=="__main__":
    part1(x)
    part2(x)
