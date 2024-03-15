"""PART 1"""
nums = set([str(i) for i in range(0,10)])
s = []

with open(r'day3.txt', 'r') as f:
    file = f.readlines()

    # Create matrix
    for i in file:
        i = i.strip()
        s.append([i[j] for j in range(len(i))])

# Check number
rows = len(s)
cols = len(s[0])

# print(s[0])
s_num_range = []

for row in range(rows):
    num_range = []
    print(s[row])
    l, r = 0, 0
    while r < rows:
        if s[row][l] in nums:
            while r < rows:
                if s[row][r] in nums:
                    r += 1
                else:
                    # print(row,l,r)
                    num_range.append([l,r])
                    # print(s[row][l:r])
                    l = r
                    break
            else:
                # print(row,l,r+1)
                num_range.append([l,r+1])
                # print(s[row][l:r+1])
                break
        else:
            l += 1
            r = l
    s_num_range.append(num_range)
# print(s_num_range[20])

res = []

for row in range(len(s_num_range)):
    for l, r in s_num_range[row]:
        # print(s[row][l:r])
        r_lim = rows - 1 if r >= rows else r 
        l_lim = 1 if l == 0 else l

        if row == 0:
            row_range = range(0,2)    
        elif row >= rows - 1:
            row_range = range(-1,1)
        else:
            row_range = range(-1,2)

        flag = False
        for i in range(l_lim-1, r_lim+1):
            for j in row_range:
                # print(i)
                if s[row+j][i] != '.' and s[row+j][i] not in nums:
                    flag = True
                    # print(int(''.join(s[row][l:r])))
        if flag:
            res.append(int(''.join(s[row][l:r])))
            # res += int(''.join(s[row][l:r]))
            
        # print(s[row-1][l-1:r+1])
        # print(s[row][l-1:r+1])
        # print(s[row+1][l-1:r+1])

print(sum(res))

"""PART 2"""
gears = {}
res_2 = []

for row in range(len(s_num_range)):
    for l, r in s_num_range[row]:
        # print(s[row][l:r])
        r_lim = rows - 1 if r >= rows else r 
        l_lim = 1 if l == 0 else l

        if row == 0:
            row_range = range(0,2)    
        elif row >= rows - 1:
            row_range = range(-1,1)
        else:
            row_range = range(-1,2)

        for i in range(l_lim-1, r_lim+1):
            for j in row_range:
                # print(i)
                if s[row+j][i] == '*':
                    gear_idx = (row+j, i)
                    val = int(''.join(s[row][l:r]))
                    
                    if gears.get(gear_idx):
                        g_1 = gears.get(gear_idx)
                        g_2 = val
                        res_2.append(g_1 * g_2)
                    else:
                        gears[gear_idx] = val
                    # print(int(''.join(s[row][l:r])), (row+j, i))
                    # print(int(''.join(s[row][l:r])))


print(sum(res_2))