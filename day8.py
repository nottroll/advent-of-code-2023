import math

#----------PART 1----------#

net = {}

with open(r'day8.txt', 'r') as f:
    file = f.readlines()
    
    n = file[0].strip()
    nav = [n[i] for i in range(len(n))]

    for line in file[2:]:
        k = line[0:3]
        v = line[7:10], line[12:15]
        net[k] = v
    
    print(nav)
    print(net)

start = 'AAA'
end = 'ZZZ'

i = 0
curr = start
while True:
    next = nav[i % len(nav)]
    # print(i, next, curr, net.get(curr))
    if next == 'L':
        curr = net.get(curr)[0]
    else:
        curr = net.get(curr)[1]
    i += 1
    if curr == end:
        break

print(i)

#----------PART 2----------#
starting = []
ending = []

for i in net.keys():
    if i[-1] == 'A':
        starting.append(i)

print(starting)

cycles = []

for i in starting:
    # print(i, end)
    step = 0
    curr = i
    while True:
        next = nav[step % len(nav)]
        # print(i, next, curr, net.get(curr))
        if next == 'L':
            curr = net.get(curr)[0]
        else:
            curr = net.get(curr)[1]
        step += 1
        if curr[-1] == 'Z':
            cycles.append(step)
            break

print(cycles)

print(math.lcm(22411, 18727, 24253, 14429, 16271, 20569))