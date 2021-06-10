s1 = input()
s2 = input()
arr1 = s1.split()
arr2 = s2.split()
res = list(set(arr1) & set(arr2))
for i in range(0,len(res)):
    res[i] = int(res[i])
res.sort()
for i in range(len(res)-1):
    print(res[i], end = " ")
print(res[len(res)-1])