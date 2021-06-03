with open("input.txt", "r") as file:
    lines = file.readlines()

a = int(lines[0].split()[0])
b = int(lines[1].split()[0])
c = int(lines[2].split()[0])
result = 'NO'

if a+b>c and a+c>b and b+c>a:
    result = 'YES'



with open("output.txt", "w") as file:
    file.write(result)
