s = input()
numbers = s.split(' ')
result = 0
for i in range(1, len(numbers)-1):
    if int(numbers[i])>int(numbers[i-1]) and int(numbers[i])>int(numbers[i+1]):
        result += 1

print(result)