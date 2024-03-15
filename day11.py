
#----------PART 1----------#
stars = []
expand_row = []


with open(r'day11.txt', 'r') as f:
    file = f.readlines()

    col_empty = [True for _ in range(len(file))]

    for row in range(len(file)):
        cols = file[row]
        row_empty = True
        for i in range(len(cols)):
            if cols[i] == '#':
                stars.append((i, row))
                row_empty = False
                col_empty[i] = False
        if row_empty:
            expand_row.append(row)
    
    expand_col = [i for i in range(len(col_empty)) if col_empty[i]]

print(stars)
print(expand_row)
print(expand_col)

res = 0
for i in range(len(stars) - 1):
    for j in range(i + 1, len(stars)):
        d = abs(stars[i][0] - stars[j][0]) + abs(stars[i][1] - stars[j][1])
        for ex_row in expand_row:
            m = max(stars[i][1], stars[j][1])
            n = min(stars[i][1], stars[j][1])
            if n < ex_row < m:
                d += 1  # set as 999999 for part 2
        for ex_col in expand_col:
            m = max(stars[i][0], stars[j][0])
            n = min(stars[i][0], stars[j][0])
            if n < ex_col < m:
                d += 1  # set as 999999 for part 2
        
        res += d
        # print(i, j, d)
print(res)

#----------PART 2----------#
