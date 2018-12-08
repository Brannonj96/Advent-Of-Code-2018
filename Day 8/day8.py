from inputday8 import *

#format input to be a list of integers
x = list(map(int,x.split()))
#id for our dictionary
ID = 0 

def makeTree( inp, tree = {}, parent=None):
    global ID

    #If there is a parent add this node to its children
    if parent!=None:
        tree[parent][0].append(ID)

    #This will be children, metadata entries
    tree[ID] = [[],[]]
    #save the parent's id
    cur = ID

    #Inc the global ID to get a unique value for each node
    ID+=1
    #First two values will be the children and meta
    chil, meta = inp[0], inp[1]

    #Once we get it, delete them so the relevant info is next
    del inp[0]
    del inp[0]

    #Repeat this and add new nodes for however many children we got
    for i in range(chil):
        #The returned inp will be the current nodes meta data first
        #the metadata loop deletes all the meta data and readies up
        #for the next node
        inp,tree = makeTree(inp, tree, cur)

    #Add all the meta data entries
    for i in range(meta):
        #add the data to the metadata list
        tree[cur][1].append(inp[0])
        #delete the data entry
        del inp[0]

    #return the inp and tree where tree is our current knowledge
    #and inp has the next relevant info first in the list
    return inp,tree

def calcValue(tree,node=0):

    #If no children return the sum
    if not tree[node][0]:

        return sum(tree[node][1])
    else:
        #Else calculate the value of the current nodes
        #children where the child's index is the metadata value - 1
        s=0
        #loop through all metadata
        for eachData in tree[node][1]:
            
            #If the metadata is smaller than the size of the children list
            #i.e. current node actually has an Nth child
            if eachData <= (len(tree[node][0])):

                #Then get the Nth child and
                nextNode = tree[node][0][eachData-1]

                #calcualte it's sum and add it to this nodes
                #value
                s+= calcValue(tree, nextNode)
        #return value
        return s



#the returned inp will be an empty list, so don't store it
_, tree = makeTree(x)


#calculate the sum of all metadata entries
s=0
for i in tree:
    s+= sum(tree[i][1])

print(s)

#Calculate the node's value (default is starting at root node)
print(calcValue(tree))     
    
            
            
        
