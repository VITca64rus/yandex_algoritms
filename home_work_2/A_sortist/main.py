s = input()
numbers = s.split(' ')
def check(numbers):
    min = int(numbers[0])
    for i in range(1, len(numbers)):

        if int(numbers[i]) > min:
            min = int(numbers[i])
        else:
            return('NO')
    return('YES')

print(check(numbers))
