
#----------PART 1----------#

with open(r'day15.txt', 'r') as f:
    file = f.readlines()

    s = file[0].strip().split(',')

# print(s)
res = []

for i in s:
    val = 0
    for j in range(len(i)):
        val += ord(i[j])
        val *= 17
        val %= 256
    res.append(val)

print(sum(res))

#----------PART 2----------#
s_2 = []
for i in s:
    if i[-2] == '=':
        a = i.split('=')
        s_2.append([a[0], int(a[1])])
    else:
        s_2.append(i[:-1])

print(s_2)

def hash(s: str) -> int:
    val = 0
    for j in range(len(s)):
        val += ord(s[j])
        val *= 17
        val %= 256
    return val

hashmap = {}

for i in s_2:
    if type(i) == list:
        box_num = hash(i[0])
        if hashmap.get(box_num):
            lst = hashmap.get(box_num)
            for j in range(len(lst)):
                if i[0] == lst[j][0]:
                    lst[j] = i
                    hashmap[box_num] = lst
                    break
            else:
                hashmap[box_num] += [i]
        else:
            hashmap[box_num] = [i]
        # print(box_num)
    else:
        for k,v in hashmap.items():
            for j in range(len(v)):
                if i == v[j][0]:
                    v.pop(j)
                    break

    # print(hashmap)

res = 0
for k, v in hashmap.items():
    for i in range(len(v)):
        # print(v[i][1])
        res += (k + 1) * (i + 1) * v[i][1]

print(res)