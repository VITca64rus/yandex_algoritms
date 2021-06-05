n = int(input())
s = input()
numbers = s.split()

def simm(posl):
    i = 0
    j = len(posl)-1
    while j - i >= 1:

        if posl[i] == posl[j]:
            i += 1
            j -= 1
        else:
            return 0
    return 1

for i in range(0,n):
    numbers[i] = int(numbers[i])


def find_idx(posl):
    el = posl[-1:]
    idxs = []
    for i in range(0,len(posl)):
        if posl[i]==el[0]:
            idxs.append(i)
    return idxs

def get_answ(idx,numbers):
    for id in idx:
        symbols = numbers[0:id]
        symbols = symbols[::-1]
        result = numbers + symbols

        if simm(result) == 1:
            return symbols

if simm(numbers) == 0:
    idx = find_idx(numbers)

    res = (get_answ(idx,numbers))
    ss=''
    for s in res:
        ss = ss+str(s)+' '
    print(len(res))
    print(ss[:-1])
else:
    print(0)
