n = int(input())
s = input()
numbers = s.split(' ')
x = int(input())
result = int(numbers[0])
razn = abs(int(numbers[0]) - x)

for i in range(1,n):
    if abs(int(numbers[i]) - x) < razn:
        result = numbers[i]
        razn = abs(int(numbers[i]) - x)

print(result)
