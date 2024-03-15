
#----------PART 1----------#
field = []

with open(r'day14.txt', 'r') as f:
    file = f.readlines()
    field = [[line[i] for i in range(len(line)-1)] for line in file]

def transpose(field):
    rows = len(field)
    cols = len(field[0])
    field_col = [[] for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            field_col[col].append(field[row][col])
    return field_col

def move_n(field):
    field_col = transpose(field)

    moved_field = []
    for f in field_col:
        round_cube = [[0,-1]]
        cnt = 0
        for i in range(len(f)):
            if f[i] == 'O':
                cnt += 1
            if f[i] == '#':
                round_cube.append([cnt, i])
                cnt = 0
        round_cube.append([cnt, len(f)])

        # print(round_cube)

        moved = []
        for i in range(len(round_cube)-1):
            for _ in range(round_cube[i+1][0]):
                moved.append('O')
            for _ in range(round_cube[i+1][1]-round_cube[i][1]-round_cube[i+1][0]-1):
                moved.append('.')
            moved.append('#')
        moved.pop(-1)

        moved_field.append(moved)

    # print(transpose(moved_field))
    # print()
    return transpose(moved_field)

def total(field):
    res = 0
    for row in range(len(field)):
        for col in range(len(field[0])):
            if field[row][col] == 'O':
                res += len(field) - row
        # print(res)
    # print(res)
    return res

# field_one = move_n(field)
# total(field_one)

#----------PART 2----------#

def move_w(field):
    moved_field = []
    for f in field:
        round_cube = [[0,-1]]
        cnt = 0
        for i in range(len(f)):
            if f[i] == 'O':
                cnt += 1
            if f[i] == '#':
                round_cube.append([cnt, i])
                cnt = 0
        round_cube.append([cnt, len(f)])

        # print(round_cube)

        moved = []
        for i in range(len(round_cube)-1):
            for _ in range(round_cube[i+1][0]):
                moved.append('O')
            for _ in range(round_cube[i+1][1]-round_cube[i][1]-round_cube[i+1][0]-1):
                moved.append('.')
            moved.append('#')
        moved.pop(-1)

        moved_field.append(moved)

    # print(moved_field)
    # print()
    return moved_field

def move_s(field):
    field_col = transpose(field)

    moved_field = []
    for f in field_col:
        round_cube = [[0,-1]]
        cnt = 0
        for i in range(len(f)):
            if f[i] == 'O':
                cnt += 1
            if f[i] == '#':
                round_cube.append([cnt, i])
                cnt = 0
        round_cube.append([cnt, len(f)])

        # print(round_cube)

        moved = []
        for i in range(len(round_cube)-1):
            for _ in range(round_cube[i+1][1]-round_cube[i][1]-round_cube[i+1][0]-1):
                moved.append('.')
            for _ in range(round_cube[i+1][0]):
                moved.append('O')
            moved.append('#')
        moved.pop(-1)

        moved_field.append(moved)

    # print(transpose(moved_field))
    # print()
    return transpose(moved_field)

def move_e(field):
    moved_field = []
    for f in field:
        round_cube = [[0,-1]]
        cnt = 0
        for i in range(len(f)):
            if f[i] == 'O':
                cnt += 1
            if f[i] == '#':
                round_cube.append([cnt, i])
                cnt = 0
        round_cube.append([cnt, len(f)])

        # print(round_cube)

        moved = []
        for i in range(len(round_cube)-1):
            for _ in range(round_cube[i+1][1]-round_cube[i][1]-round_cube[i+1][0]-1):
                moved.append('.')
            for _ in range(round_cube[i+1][0]):
                moved.append('O')
            moved.append('#')
        moved.pop(-1)

        moved_field.append(moved)

    # print(moved_field)
    # print()
    return moved_field


def n_cycle(field):
    def cycle(field):
        return move_e(move_s(move_w(move_n(field))))
    
    res_2 = []
    res_set = set()
    max_seq_len = 0
    res_seq = []

    field = cycle(field)
    weight = total(field)
    res_2.append(weight)
    res_set.add(weight)

    cont = True
    while cont == True:
    # for _ in range(n-1):
        field = cycle(field)
        weight = total(field)
        res_2.append(weight)
        res_set.add(weight)

        # print(res_2)

        if res_2[-1] in res_set:
            candidate = []
            for i in range(len(res_2)-1):
                if res_2[i] == res_2[-1]:
                    candidate.append(i)

            for idx in candidate:
                shift = 1
                while len(res_2)-1-shift > idx:
                    # print(idx, len(res_2)-1-shift, res_2[len(res_2)-1-shift],idx-shift, res_2[idx-shift])
                    if res_2[len(res_2)-1-shift] != res_2[idx-shift]:
                        # print('test')
                        break
                    shift += 1
                else:
                    # print(res_2[idx+1:])
                    if len(res_2[idx+1:]) > 2 and len(res_2[idx+1:]) > max_seq_len:
                        max_seq_len = len(res_2[idx+1:])
                        res_seq = idx + 1, len(res_2) - 1, res_2[idx+1:]
                        cont = False
                        break
    print(res_seq)

    return field, res_2, res_seq

seq = n_cycle(field)[2][2]

# total(field_two)

# [87, 69, 69, 69, 65, 64, 65, 63, 68, 69, 69, 65, 64, 65, 63, 68, 69, 69, 65, 64, 65, 63, 68]

# n = (1000000000 - 9) % (15 - 9 + 1)
# print(n)

# [103205, 103031, 103035, 103148, 103165, 103244, 103271, 103336, 103413, 103517, 103660, 103767, 103839, 103902, 103957, 103985, 104000, 104080, 104144, 104171, 104174, 104234, 104280, 104329, 104381, 104452, 104487, 104538, 104589, 104653, 104717, 104754, 104805, 104844, 104870, 104879, 104905, 104936, 104970, 105017, 105079, 105131, 105194, 105257, 105309, 105350, 105398, 105431, 105469, 105519, 105552, 105564, 105576, 105562, 105545, 105526, 105504, 105514, 105494, 105478, 105470, 105457, 105484, 105510, 105551, 105598, 105614, 105662, 105680, 105710, 105751, 105770, 105793, 105812, 105844, 105887, 105925, 105953, 105954, 105948, 105949, 105935, 105935, 105918, 105884, 105855, 105812, 105788, 105758, 105730, 105727, 105694, 105684, 105670, 105650, 105661, 105654, 105642, 105625, 105606]

n = (1000000000 - 159) % (223 - 159 + 1)
print(n)

print(seq[n-1])