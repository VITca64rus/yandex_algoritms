str_data = input()
a1, b1, a2, b2 = str_data.split()
a1 = int(a1)
a2 = int(a2)
b1 = int(b1)
b2 = int(b2)


stols = []
stols.append((a1+a2, max(b1,b2)))
stols.append((a1+b2, max(b1,a2)))
stols.append((max(a1, a2), b1 + b2))
stols.append((max(a1, b2), b1 + a2))

i_max = 0
i = 0
for stol in stols:

    if stol[0]*stol[1] < stols[i_max][0]*stols[i_max][1]:
        i_max = i
    i += 1

print(stols[i_max][0], stols[i_max][1])






