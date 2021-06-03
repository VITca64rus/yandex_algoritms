with open("input.txt", "r") as file:
    lines = file.readlines()


change_lines = []

for line in lines:
    line = line.replace('-', '')
    line = line.replace ('+7', '8')
    line = line.replace ('(', '')
    line = line.replace (')', '')
    if line[0] != '8':
        line = '8495' + line
    change_lines.append(line)
#print(change_lines)

for i in range(1,4):
    if change_lines[0] == change_lines[i]:
        change_lines[i] = 'YES\n'
    else:
        change_lines[i] = 'NO\n'

change_lines = change_lines[1:]
#print(change_lines)


with open("output.txt", "w") as file:
    file.writelines(change_lines)