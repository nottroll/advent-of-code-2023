
#----------PART 1----------#

with open(r'day9.txt', 'r') as f:
    file = f.readlines()
    seq = [[int(j) for j in i.split()] for i in file]
            

res = []

for i in seq:
    sub_seq = [i]
    while True:
        curr = sub_seq[-1]
        next = []
        for i in range(len(curr)-1):
            next.append(curr[i+1] - curr[i])

        sub_seq.append(next)
        if sum(next) == 0:
            r = 0
            for j in sub_seq:
                r += j[-1]
            res.append(r)
            break

print(sum(res))

#----------PART 2----------#

print(seq[0])

res = []
for i in seq:
    sub_seq = [i]
    while True:
        curr = sub_seq[-1]
        next = []
        for i in range(len(curr)-1):
            next.append(curr[i+1] - curr[i])
        sub_seq.append(next)
        # print(next)
        if sum(next) == 0:
            r = 0
            for j in range(1, len(sub_seq)):
                print(r, sub_seq[-j][0])
                r = sub_seq[-j][0] - r
                
            res.append(sub_seq[0][0] - r)
            break

print(sum(res))