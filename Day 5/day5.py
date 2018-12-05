from inputday5 import *
import re


#GOT SOME USELESS VARIABLES HERE. WOOPS
i=0
print(x[-5:])
s=x
prev = x
l=1
f=1
#= list('dabAcCaCBAcCcaDA')

if f!=2:
    f=1
i=0

#print(x[:20])
min=None
#s= 'dabAcCaCBAcCcaDA'

#REMOVE EACH LETTER PAIR FOR PART 2 AND TRY AGAIN
for each in set(x):
    #print('\ndeleting',each,'\n')
    x= s.replace(each.lower(),'')
    x  = list(x.replace(each.upper(),''))
    l = len(x)-1
    i=0
    #print(x)

    #BELOW CODE IS PART 1
    while i<l:
        #print(x)
        #print(len(x))
        if x[i].isupper():
            if x[i].lower()==x[i+1]:
                del x[i]
                del x[i]
                i= max(0,i-1)
                l-=2
                f=0
                continue
        if x[i+1].isupper():
            if x[i] == x[i+1].lower():
                del x[i]
                del x[i]
                i = max(0,i-1)
                l-=2
                f=0
                continue
        i+=1

    #THIS IS FOR PART 2
    if min==None:
        min = len(x)
    elif len(x)<min:
        min = len(x)

#PRINT LEN(X) FOR PART 1
print(min)
    
    

