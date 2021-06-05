s = input()
numbers = s.split(' ')

max1 = min(int(numbers[0]), int(numbers[1]))
max2 = max(int(numbers[0]), int(numbers[1]))

min1 = max1
min2 = max2

max2_i = 0
min1_i = 0
for i in range(2, len(numbers)):
    numbers[i] = (int(numbers[i]))
    if numbers[i] > max2:
        max1 = max2
        max2 = numbers[i]
        max2_i = i

    if max1 < numbers[i] <= max2 and i != max2_i:
        max1 = numbers[i]

    if numbers[i] < min1:
        min2 = min1
        min1 = numbers[i]
        min1_i = i
    if min1 <= numbers[i] < min2 and i != min1_i:
        min2 = numbers[i]

if max1 * max2 > min1 * min2:
    print(max1, max2)
else:
    print(min1, min2)
