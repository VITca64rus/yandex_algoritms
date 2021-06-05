n = int(input())
s = input()
numbers = s.split(' ')
for i in range(0, n):
    numbers[i] = int(numbers[i])

pobed = max(numbers)

def get_id_pobed(numbers,n):
    res=[]
    for i in range(0, n):
        if numbers[i]==pobed:
            res.append(i)
    return min(res)

id_pobed = get_id_pobed(numbers,n)


def get_meters_vasy(numbers,id_pobed, n):
    result = 1001
    for i in range(1, n-1):
        if (str(numbers[i])[-1:] == '5') and (numbers[i+1] < numbers[i]) and (i < id_pobed):
            result = numbers[i]
    return result


def get_pos(n, numbers, vas_res):
    for i in range(0,n):
        if numbers[i] == vas_res:
            return i+1


vas_res = get_meters_vasy(numbers, pobed, n)
if vas_res != 1001:
    numbers.sort(reverse=True)
    print(get_pos(n, numbers, vas_res))
else:
    print(0)
