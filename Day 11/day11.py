
def part1():

    grid = []
    for i in range(300):
        grid.append([])
        for j in range(300):
            rackId = j+11
            p = rackId*(i+1)
            p+=7400
            p *= rackId
            p = int(str(p)[-3])-5
            grid[i].append(p)

    m = 0

    for a in range(1,301):
        print(a)
        for i in range(300-a):
            for j in range(300-a):
                s = 0
                for k in range(a):
                    for l in range(a):
                        s+= grid[j+l][i+k]
                if s>m:
                    m = s
                    coord = (i+1, j+1)
                    size = a
                    #print(m)
                    print(coord,s)


part1()
