from inputday4 import *
import re
from datetime import datetime

date_format = "%Y,%m,%d %H:%M"
getAllInts = lambda s: map(int, re.findall(r'-?\d+', s))

x = sorted(x, key = lambda a: (list(map(abs, getAllInts(a)))[0],
                               list(map(abs, getAllInts(a)))[1],
                               list(map(abs, getAllInts(a)))[2],
                               list(map(abs, getAllInts(a)))[3],
                               list(map(abs, getAllInts(a)))[4]))
y = list(map(lambda s: map(int, re.findall(r'-?\d+', s)), x))
getAllInts = lambda s: map(int, re.findall(r'-?\d+', s))
guards = dict()

lastg = None
lastT = []
for each in x:
    line = list(getAllInts(each))
    year = line[0]
    month = abs(line[1])
    day = abs(line[2])
    hour = line[3]
    minute = line[4]
    if len(line)==6:
        lastg = line[-1]
        if line[-1] not in guards:
            guards[line[-1]] = [0, dict()]

    #print(each.split()[2])
    if each.split()[2]=='wakes':
        slept = datetime.strptime(','.join(map(str,[year, month, day]))+' '+':'.join([str(hour),str(minute)]), date_format)
        minutesSlept = int(str((slept-lastT)).split(':')[1])
        #print(minutesSlept)
        guards[lastg][0]+= minutesSlept

        lastM = int(str(lastT).split(':')[1])
        
        for i in range(minutesSlept):
            if lastM+i not in guards[lastg][1]:
                guards[lastg][1][(lastM+i)%60] = 0
            guards[lastg][1][(lastM+i)%60] += 1
        
        #print('Guard',lastg,'slept a total of',guards[lastg])
        continue
    elif each.split()[2]=='falls':
        lastT =  datetime.strptime(','.join(map(str,[year, month, day]))+' '+':'.join([str(hour),str(minute)]), date_format)
"""
highest = 0
id = 0
for each in guards:
    if guards[each][0]>highest:
        highest = guards[each][0]
        id = each
minut=0
newId = 0
for each in guards[id][1]:
    if guards[id][1][each]>minut:
        minut = guards[id][1][each]
        newId = each
        print(minut)
print(minut, newId)
print(id, newId)
print(id*newId)"""

id = 0
max = 0
minute = 0
for each in guards:
    for eachMinute in guards[each][1]:
        if guards[each][1][eachMinute]>max:
            max = guards[each][1][eachMinute]
            minute = eachMinute
            id = each
print(id, max, minute)
print(id*minute)

    
        


        
        
