n = int(input())
s = input()
numbers = s.split(' ')
for i in range(0, n):
    numbers[i] = int(numbers[i])

pobed = max(numbers)
#print('Бросок победителя - ',pobed)

def get_id_pobed(numbers,n):
    res=[]
    for i in range(0, n):
        if numbers[i]==pobed:
            res.append(i)
    return min(res)

id_pobed = get_id_pobed(numbers,n)
#print('ИД победителя - ',id_pobed)


def get_meters_vasy(numbers,id_pobed, n):
    result = []
    for i in range(id_pobed+1, n-1):

        if (str(numbers[i])[-1:] == '5') and (numbers[i+1] < numbers[i]):
            result.append(numbers[i])
    if result:
        return max(result)
    else:
        return 1001


def get_pos(n, numbers, vas_res):
    for i in range(0,n):
        if numbers[i] == vas_res:
            return i+1


vas_res = get_meters_vasy(numbers, id_pobed, n)
#print(vas_res)
if vas_res != 1001:
    numbers.sort(reverse=True)
    print(get_pos(n, numbers, vas_res))
else:
    print(0)
