import math

"""PART 1"""

with open(r'day6.txt', 'r') as f:
    file = f.readlines()

    time = [int(i) for i in file[0].split()[1:]]
    dist = [int(i) for i in file[1].split()[1:]]

res = 1

for total_t, record_d in zip(time,dist):
    print(total_t, record_d)
    cnt = 0
    for t in range(1, total_t):
        speed = t
        d = speed * (total_t - t)
        if d > record_d:
            cnt += 1
    res *= cnt

print(res)

"""PART 2"""

time_2 = int(''.join(str(i) for i in time))
dist_2 = int(''.join(str(i) for i in dist))

print(time_2, dist_2)

upper = (time_2 + math.sqrt((time_2 * time_2) - (4 * dist_2))) / 2
lower = (time_2 - math.sqrt((time_2 * time_2) - (4 * dist_2))) / 2

print(upper,lower)

print(9701199 * (time_2-9701199) > dist_2)
print(49295270 * (time_2-49295270) > dist_2)

print(int(upper) - math.ceil(lower) + 1)
