a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

result = 'NO'

if ((a<=d) and (b<=e)) or ((a<=e) and (b<=d)):
    result = 'YES'

if ((b<=d) and (c<=e)) or ((b<=e) and (c<=d)):
    result = 'YES'

if ((c<=d) and (a<=e)) or ((c<=e) and (a<=d)):
    result = 'YES'

print(result)
