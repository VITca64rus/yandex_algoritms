a, b, c = int(input()), int(input()), int(input())
if c < 0 or (a == 0 and b != c**2):
    print('NO SOLUTION')
elif (a == 0 and b == c**2) or a == b == c == 0:
    print('MANY SOLUTIONS')
else:
    if (c**2 - b) % a == 0:
        print(int((c**2 - b) / a))
    else:
        print ('NO SOLUTION')
