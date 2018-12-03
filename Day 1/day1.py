from inputday1 import *
#print(sum([int(i) for i in x.split('\n')]))
nums = set()
s=0
f=True
while f:
    for each in x.split('\n'):
        s+=int(each)
        if s in nums:
            print(s)
            f=False
            break
        nums.add(s)
    
