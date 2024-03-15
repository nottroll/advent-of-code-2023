
#----------PART 1----------#

boards = []

with open(r'day13.txt', 'r') as f:
    file = f.readlines()

    next = False
    board = []
    for line in file:
        if len(line) > 1:
            board.append([line[i] for i in range(len(line) - 1)])
        else:
            boards.append(board)
            board = []
        

res = []

for board in boards:
    # print()
    rows = len(board)
    cols = len(board[0])
    cols_list = [[] for _ in range(cols)]

    # Check rows
    row_candidates = []
    for row in range(rows - 1):
        if board[row] == board[row + 1]:
            row_candidates.append(row)
            # print('r', row, row+1)
        
        for col in range(cols):
            cols_list[col].append(board[row][col])

    for col in range(cols):
        cols_list[col].append(board[-1][col])

    # print(cols_list)

    # Check cols
    col_candidates = []
    for col in range(cols - 1):
        if cols_list[col] == cols_list[col + 1]:
            col_candidates.append(col)
            # print('c',col, col+1)

    # print('r_can', row_candidates)

    if len(row_candidates) == 1 and len(col_candidates) == 0:
        res.append((row_candidates[0]+1) * 100)
    else:
        shifts = [0]
        for candidate in row_candidates:
            shift = 1
            # print(candidate)
            while candidate + 1 + shift < rows and candidate - shift >= 0:
                # print(''.join(board[candidate + 1 + shift]), ''.join(board[candidate - shift]))
                if board[candidate + 1 + shift] != board[candidate - shift]:
                    break
                shift += 1
            else:
                # print('TEST')
                res.append((candidate+1) * 100)

    # print('c_can', col_candidates)

    if len(col_candidates) == 1 and len(row_candidates) == 0:
        res.append(col_candidates[0]+1)
    else:
        shifts = [0]
        for candidate in col_candidates:
            shift = 1
            # print(candidate)
            while candidate + 1 + shift < cols and candidate - shift >= 0:
                # print(''.join(cols_list[candidate + 1 + shift]), ''.join(cols_list[candidate - shift]))
                if cols_list[candidate + 1 + shift] != cols_list[candidate - shift]:
                    # print('FAIL')
                    break
                shift += 1
            else:
                # print('ADD')
                res.append(candidate+1)

# print(res)
# print(sum(res))

#----------PART 2----------#

res_2 = []
cnt = 0

for board in boards:
    print()
    rows = len(board)
    cols = len(board[0])
    cols_list = [[] for _ in range(cols)]

    # Check rows
    row_candidates = []
    for row in range(rows - 1):
        # print('check r', row, ''.join(board[row]), row+1, ''.join(board[row+1]))
        off_by = 0
        shift = 0
        # print(off_by, shift)
        while off_by <= 1 and row + 1 + shift < rows and row - shift >= 0:
            for char in range(len(board[row])):
                # print(board[row - shift][char], board[row + 1 + shift][char])

                if board[row - shift][char] != board[row + 1 + shift][char]:
                    off_by += 1
            shift += 1
        else:
            if off_by == 0:
                print('full sym',row)
            if off_by == 1:
                res_2.append((row + 1)*100)
                print('off by 1 sym', row)
        
        for col in range(cols):
            cols_list[col].append(board[row][col])

    for col in range(cols):
        cols_list[col].append(board[-1][col])

    # Check cols
    col_candidates = []
    for col in range(cols - 1):

        # print('check c', col, ''.join(cols_list[col]), col+1, ''.join(cols_list[col+1]))
        off_by = 0
        shift = 0
        # print(off_by, shift)
        while off_by <= 1 and col + 1 + shift < cols and col - shift >= 0:
            for char in range(len(cols_list[col])):
                # print(cols_list[col - shift][char], cols_list[col + 1 + shift][char])

                if cols_list[col - shift][char] != cols_list[col + 1 + shift][char]:
                    off_by += 1
            shift += 1
        else:
            if off_by == 0:
                print('full sym',col)
            if off_by == 1:
                res_2.append(col + 1)
                print('off by 1 sym', col)

    # cnt += 1
    # if cnt == 2:
    #     break

print(res_2)
print(sum(res_2))
print(len(res_2))