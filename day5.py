"""PART 1"""
maps = []

with open(r'day5.txt', 'r') as f:
    file = f.readlines()

    seeds = [int(i) for i in file[0].split()[1:]]
    seeds_2 = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

    l, r = 1, 1
    while r < len(file):
        if file[l][-5:].strip() == 'map:':
            map = []
            r = l + 1
            while r < len(file):
                read_line = file[r].strip()
                if read_line:
                    n = tuple(int(i) for i in read_line.split())
                    map.append(n)
                    r += 1
                else:
                    l = r
                    maps.append(map)
                    break
        else:
            l += 1
            r = l

# print(seeds, maps[0])
# print(seeds)

res = seeds
# res = [74139777, 74139777+106006724-1]
for idx, s in enumerate(res):
    for m in maps:
        # print('map',m)
        # m = maps[0]
        s = res[idx]
        for dest, src, rn in m:
            # print(dest, src, rn)
            if src <= s < src + rn:
                res[idx] = s - src + dest
                break
            else:
                res[idx] = s

        # print(res)
# print(min(res))

"""PART 2"""
res_2 = []
for s in seeds_2:
    next = [(s[0], s[0] + s[1])]
    print(next)

    for m in maps:
        for dest, src, rn in m:
            seed_rn = []
            print(dest, src, rn)

            # SPLIT INTO RANGES
            for start, end in next:
                if src <= start < src + rn:
                    if src <= end < src + rn:
                        # start and end fully inside
                        # map whole range
                        print('fully inside',(start, end))
                        seed_rn.append((start, end))
                    else:
                        # start inside, end outside
                        # map inside
                        print('start in, end out',(start, src + rn), (src + rn, end))
                        seed_rn.append((start, src + rn))
                        seed_rn.append((src + rn, end))
                else:
                    if src <= end < src + rn:
                        print('start out, end in',(start, src), (src, end))
                        seed_rn.append((start, src))
                        seed_rn.append((src, end))
                    else:
                        # not in range, no mapping
                        print('not in',(start, end))
                        seed_rn.append((start, end))
            next = seed_rn
            print(next, '\n')

        # MAP EACH RANGE
        print('-----MAP-----')
        map_seed = []
        for start, end in next:
            for dest, src, rn in m:
                map_start = start - src + dest
                map_end = end - src + dest

                if src <= start and end <= src + rn:
                    map_seed.append((map_start, map_end))
                    break
            else:
                map_seed.append((start, end))
        print(map_seed)
        next = map_seed
    res_2.append(next)

print(res_2)

# GET MIN
min_seed = []
for i in res_2:
    min_seed.append(min(i, key=lambda start: start[0]))

res = min(min_seed, key=lambda start: start[0])
print(res)