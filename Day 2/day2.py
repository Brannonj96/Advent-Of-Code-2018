from inputday2 import *
"""
y = x.split('\n')
print(y[0])
twoBool = False
threeBool = False
two = 0
three = 0
for i in y:
    for j in set(i):
        if i.count(j)==3 and not threeBool:
            #print(i,j, 'three')
            three+=1
            threeBool = True
        if i.count(j)==2 and not twoBool:
            #print(i,j,'two')
            two+=1
            twoBool = True
    threeBool = False
    twoBool = False
        


print(two,three)"""


y = x.split('\n')

for each in range(len(y)):
    for anotherEach in range(len(y)):
        dif = 0
        letters = []
        if each == anotherEach:
            continue
        for i in range(len(y[each])):
            #print(y[each], y[anotherEach])
            if y[each][i] != y[anotherEach][i]:
                dif +=1
            else:
                #print(y[each][i], y[anotherEach][i])
                letters.append(y[each][i])
        
        if dif==1:
            print(''.join(letters))
            #print(y[each])
            break


        

