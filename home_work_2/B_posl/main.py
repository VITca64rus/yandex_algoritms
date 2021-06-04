posl = []
s = int(input())

while s != -2000000000:
    posl.append(s)
    s = int(input ())


def const(posl):
    count = posl[0]
    for i in range(1, len(posl)):
        if posl[i]!=count:
            return 0
    return 'CONSTANT'

def weak_ascending(posl):
    count = posl [0]
    for i in range (1, len (posl)):
        if posl [i] >= count:
            count = posl [i]
        else:
            return 0
    return 'WEAKLY ASCENDING'

def weak_desscending(posl):
    count = posl [0]
    for i in range (1, len (posl)):
        if posl [i] <= count:
            count = posl [i]
        else:
            return 0
    return 'WEAKLY DESCENDING'

def ascending(posl):
    count = posl[0]
    for i in range (1, len (posl)):
        #print(posl[i],count)
        if posl [i] > count:
            count = posl[i]
        else:
            return 0
    return 'ASCENDING'

def descending(posl):
    count = posl[0]
    for i in range (1, len (posl)):
        #print(posl[i],count)
        if posl [i] < count:
            count = posl[i]
        else:
            return 0
    return 'DESCENDING'

def check(posl):
    if const(posl) != 0:
        return('CONSTANT')
    if ascending(posl) != 0:
        return 'ASCENDING'
    if weak_ascending(posl) != 0:
        return 'WEAKLY ASCENDING'
    if descending(posl) != 0:
        return 'DESCENDING'
    if weak_desscending(posl) != 0:
        return 'WEAKLY DESCENDING'
    return 'RANDOM'

if len(posl)>0:
    print(check(posl))
else:
    print('RANDOM')





