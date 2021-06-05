s = input()
N, M, K = s.split()
N = int(N)
M = int(M)
K = int(K)

pole = []
for i in range(0, N):
    pole.append([None] * M)

for i in range(0, K):
    s = input()
    arr = s.split()
    pole[int(arr[0])-1][int(arr[1])-1] = '*'

for j in range(0, len(pole)):

    for i in range(0, len(pole[0])):

        if pole[j][i] is None:
            res = 0
            try:
                if pole[j][i-1] == '*' and i-1 >= 0:
                    res +=1
            except:
                pass

            try:
                if pole[j][i+1] == '*':
                    res +=1
            except:
                pass


            try:
                if pole[j-1][i] == '*' and j-1>=0:
                    res +=1
            except:
                pass

            try:
                if pole[j+1][i] == '*':
                    res +=1
            except:
                pass



            try:
                if pole[j-1][i-1] == '*' and i-1 >= 0 and j-1>=0:
                    res +=1
            except:
                pass

            try:
                if pole[j-1][i+1] == '*' and j-1>=0:
                    res +=1
            except:
                pass



            try:
                if pole[j+1][i-1] == '*' and i-1 >= 0:
                    res +=1

            except:
                pass

            try:
                if pole[j+1][i+1] == '*':
                    res +=1
            except:
                pass


            pole[j][i] = res


for st in pole:
    ss = ''
    for s in st:
        ss = ss+str(s)+' '
    print(ss[:-1])

