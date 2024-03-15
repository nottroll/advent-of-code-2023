

#----------PART 1----------#

with open(r'day10.txt', 'r') as f:
    file = f.readlines()
    matrix = [[i.strip()[j] for j in range(len(i.strip()))] for i in file]

rows = len(matrix)
cols = len(matrix[0])

# Find the start
for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'S':
            start = col, row
            # print(start, matrix[row][col])

dir = {'|':{'N':'N', 'S':'S'},
       '-':{'E':'E', 'W':'W'},
       'L':{'S':'E', 'W':'N'},
       'J':{'S':'W', 'E':'N'},
       '7':{'N':'W', 'E':'S'},
       'F':{'N':'E', 'W':'S'}}

start_x, start_y = start
path = [(start_x, start_y, 'S')]
res = []

# for x, y, start_dir in [(start_x, start_y-1, 'N'), (start_x+1, start_y, 'E'),
#                         (start_x, start_y+1, 'S'), (start_x-1, start_y, 'W')]: 

for x, y, start_dir in [(start_x, start_y+1, 'S')]:

    curr_x, curr_y = x, y
    curr_vec = start_dir

    count = 1
    # for _ in range(20):
    while True:
        # print(matrix[curr_y][curr_x])
        
        curr_pipe = matrix[curr_y][curr_x]

        path.append((curr_x, curr_y, curr_pipe))
        
        if dir.get(curr_pipe):
            curr_vec = (dir.get(curr_pipe)).get(curr_vec)
        else:
            break

        if curr_vec == 'N':
            next_x, next_y = curr_x, curr_y-1
        elif curr_vec == 'E':
            next_x, next_y = curr_x+1, curr_y
        elif curr_vec == 'S':
            next_x, next_y = curr_x, curr_y+1
        elif curr_vec == 'W':
            next_x, next_y = curr_x-1, curr_y
        else:
            break
        
        next_pipe = matrix[next_y][next_x]

        if next_pipe in ['S', '.']:
            break

        # print(curr_pipe, next_x, next_y, next_pipe, dir.get(next_pipe))

        curr_x, curr_y = next_x, next_y
        count += 1

    res.append(count // 2 + 1)

# print(path)
# print(res)


#----------PART 2----------#
row_dict = {}

for x, y, dir in path:
    if row_dict.get(y):
        row_dict[y] += [(x, dir)]
    else:
        row_dict[y] = [(x, dir)]

# print(row_dict)

for row, cols in row_dict.items():
    row_dict[row] = sorted(row_dict[row], key=lambda x: x[0])

# print(row_dict)

# for row, cols in row_dict.items():
print(row_dict[73])

cols = row_dict[73]
l, r = 0, 0

between = []
while r < len(cols) - 1:
# for _ in range(16):
    if cols[l][1] in ['|','L','J','F','7']:
        while r < len(cols) - 1:
            r += 1
            if cols[l][1] == 'L' and cols[r][1] == '7':
            if cols[l][1] == 'F' and cols[r][1] == 'J':    
            if cols[r][1] in ['|','L','J','F','7']:
                print(l, r, cols[l], cols[r], r - l - 1)
                l = r + 1
                r = l
                break
            between.append(cols[r])
    else:

        l += 1
        r = l
        # print(l, r, cols[l], cols[r])

print(between)