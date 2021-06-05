s = input()
numbers = s.split()

maxs = numbers[:3]
maxs.sort()
maxs[0] = int(maxs[0])
maxs[1] = int(maxs[1])
maxs[2] = int(maxs[2])


mins = numbers[:2]
mins.sort(reverse=True)
mins[0] = int(mins[0])
mins[1] = int(mins[1])


for i in range(2, len(numbers)):
    numbers[i] = (int(numbers[i]))
    if i>2:
        if numbers[i] > maxs[2]:
            maxs[0] = maxs[1]
            maxs[1] = maxs[2]
            maxs[2] = numbers[i]
        elif maxs[1] < numbers[i] <= maxs[2]:
            maxs[0] = maxs[1]
            maxs[1] = numbers[i]
        elif maxs[0] < numbers[i] <= maxs[1]:
            maxs[0] = numbers[i]

    if numbers[i] < mins[0]:
        mins[1] = mins[0]
        mins[0] = numbers[i]
    elif mins[0] <= numbers[i] < mins[1]:
        mins[1] = numbers[i]


if mins[0]<0 and mins[1]<0 and len(numbers)>3:
    if maxs[0] * maxs[1]*maxs[2] > (mins[0] * mins[1])*maxs[2]:
        print(maxs[0], maxs[1], maxs[2])
    else:
        print(mins[0], mins[1], maxs[2])
else:
    print (maxs [0], maxs [1], maxs [2])
