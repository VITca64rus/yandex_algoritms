with open("input.txt", "r") as file:
    lines = file.readlines()

troom = int(lines[0].split()[0])
tcond = int(lines[0].split()[1])
work = lines[1].split()[0]

if (work == 'freeze') and (tcond < troom):
    troom = tcond

if (work == 'heat') and (tcond > troom):
    troom = tcond

if work == 'auto':
    troom = tcond


with open("output.txt", "w") as file:
    file.write(str(troom))
