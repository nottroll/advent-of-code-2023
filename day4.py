"""PART 1"""
nums = set([str(i) for i in range(0,10)])
s = []

with open(r'day4.txt', 'r') as f:
    file = f.readlines()

    # Create matrix
    for i in file:
        i = i.strip()
        s.append((i[10:40].split(), i[42:].split()))

# print(s)
res = 0

for win, have in s:
    cnt = 0
    for i in win:
        for j in have:
            if i == j:
                if cnt == 0:
                    cnt = 1
                else:
                    cnt *= 2
    res += cnt

print(res)


"""PART 2"""
curr_card = 0

res_2 = [1 for _ in range(len(s))]

def play(res_2, curr_card):
    win, have = s[curr_card]
    replays = res_2[curr_card]
    cnt = 0
    for i in win:
        for j in have:
            if i == j:
                cnt += 1
    print(curr_card, cnt)
    for i in range(curr_card + 1, curr_card + cnt + 1):
        res_2[i] += 1 * replays

    # print(res_2)
    return res_2

while curr_card < len(s):
# for _ in range(4):
    # print(curr_card, res_2[curr_card])

    res_2 = play(res_2, curr_card)
    curr_card += 1
    print(res_2)

print(sum(res_2))