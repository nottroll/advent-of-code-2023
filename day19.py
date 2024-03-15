
#----------PART 1----------#

wf = {}
parts: list[dict] = []

with open(r'day19.txt', 'r') as f:
    file = f.readlines()

    l = 0
    while len(file[l]) > 2:
        line = file[l].split('{')
        wf[line[0]] = line[1][:-2].split(',')
        l += 1

    l += 1
    while l < len(file):
        part = file[l][1:-2].split(',')
        q = {}
        for p in part:
            q[p[:1]] = int(p[2:])
        parts.append(q)
        l += 1
# print(wf)
# print(parts[0])

res = []

for p in parts:
    curr = wf.get('in')
    idx = 0
    while True:
        # print(curr)

        n = p.get(curr[idx][0])
        op = curr[idx][1]
        test, if_true = curr[idx][2:].split(':')

        # print('test',n, op, test, if_true, curr, idx)

        if op == '<':
            if n < int(test):
                if if_true == 'A': 
                    res.append('A')
                    break
                elif if_true == 'R': 
                    res.append('R')
                    break
                else:
                    curr = wf.get(if_true)
                idx = 0
            else:
                idx += 1
        else:  # op == '>'
            if n > int(test):
                if if_true == 'A': 
                    res.append('A')
                    break
                elif if_true == 'R': 
                    res.append('R')
                    break
                else:
                    curr = wf.get(if_true)
                idx = 0
            else:
                idx += 1
        # print('curr',n, op, test, if_true, curr, idx)

        if idx == len(curr) - 1:
            if curr[-1] == 'A': 
                res.append('A')
                break
            elif curr[-1] == 'R': 
                res.append('R')
                break
            else:
                curr = wf.get(curr[-1])
            idx = 0

# print(res)

add = 0
for i in range(len(res)):
    if res[i] == 'A':
        for v in parts[i].values():
            add += v

# print(add)
    
#----------PART 2----------#



done = []
# ranges = [[[1,4000] for _ in range(4)] + ['in']]
ranges: list[list[dict, str]] = [[{'x':[1,4000],'m':[1,4000],'a':[1,4000],'s':[1,4000]}, 'in']]
print('START', ranges)

cnt = 0
idx = 0

while len(ranges) > 0:
    # print(cnt)
    # print()
    curr = wf.get(ranges[0][1])

    # print('CURR', bin, op, test, if_true, curr, idx)

    bin = curr[idx][0]  # x, m, a, s
    op = curr[idx][1]
    test, if_true = curr[idx][2:].split(':')
    test = int(test)

    # print('CURR', bin, op, test, if_true, curr, idx)

    r_min, r_max = ranges[0][0].get(bin)
    if r_min < test < r_max:
        r_1 = dict(ranges[0][0])
        if op == '<':
            # print([r_min, test-1])
            # print([test, r_max])

            r_1[bin] = [r_min, test-1]
            
            if if_true == 'A': 
                done.append([r_1, 'A'])
            elif if_true == 'R': 
                done.append([r_1, 'R'])
            else:
                ranges.append([r_1, if_true])
            ranges[0][0][bin] = [test, r_max]  # this one got idx += 1

            
        else:  # op == '>':

            r_1[bin] = [test+1, r_max]

            if if_true == 'A': 
                done.append([r_1, 'A'])
            elif if_true == 'R': 
                done.append([r_1, 'R'])
            else:
                ranges.append([r_1, if_true])
            ranges[0][0][bin] = [r_min, test]  # this one got idx += 1

    # print('RANGES', ranges)
    # print('DONE', done)
    
    idx += 1

    if idx == len(curr) - 1:
        if curr[-1] == 'A': 
            done.append([dict(ranges[0][0]), 'A'])
            ranges.pop(0)
        elif curr[-1] == 'R': 
            done.append([dict(ranges[0][0]), 'R'])
            ranges.pop(0)
        else:
            ranges[0][1] = curr[-1]
        idx = 0



    # cnt += 1
    # if cnt == 10:
    #     break

# print('RANGES', ranges)
# print('DONE', done)

res_2 = 0
for rg, res in done:
    print(rg, res)
    if res == 'A':
        combo = 1
        for k, v in rg.items():
            combo *= v[1] - v[0] + 1
        res_2 += combo

print(res_2)