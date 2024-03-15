
#----------PART 1----------#

field = []

with open(r'day16.txt', 'r') as f:
    file = f.readlines()

    field = [[i[j] for j in range(len(i)-1)] for i in file]

# start_x, start_y, start_vec = 0, 0, 'R'  # R, L, U, D

x_lim = len(field[0])
y_lim = len(field)

def run(start_x, start_y, start_vec):

    energised = set()
    branch = [(start_x, start_y, start_vec)]
    done = set()

    while len(branch) > 0:
        
        if branch[0] not in done:
            curr_x, curr_y, curr_vec = branch[0]

            while 0 <= curr_x < x_lim and 0 <= curr_y < y_lim:
                # print(curr_x, curr_y, curr_vec)

                energised.add((curr_x, curr_y))

                if field[curr_y][curr_x] == '/':
                    if curr_vec == 'R':
                        curr_vec = 'U'
                    elif curr_vec == 'L':
                        curr_vec = 'D'
                    elif curr_vec == 'U':
                        curr_vec = 'R'
                    elif curr_vec == 'D':
                        curr_vec = 'L'
                elif field[curr_y][curr_x] == '\\':
                    if curr_vec == 'R':
                        curr_vec = 'D'
                    elif curr_vec == 'L':
                        curr_vec = 'U'
                    elif curr_vec == 'U':
                        curr_vec = 'L'
                    elif curr_vec == 'D':
                        curr_vec = 'R'
                elif field[curr_y][curr_x] == '-' and curr_vec in ['U', 'D']:
                    # curr_vec = 'L'
                    branch.append((curr_x, curr_y, 'L'))
                    branch.append((curr_x, curr_y, 'R'))
                    b = branch.pop(0)
                    done.add(b)
                    break

                elif field[curr_y][curr_x] == '|' and curr_vec in ['L', 'R']:
                    # curr_vec = 'U'
                    branch.append((curr_x, curr_y, 'U'))
                    branch.append((curr_x, curr_y, 'D'))
                    b = branch.pop(0)
                    done.add(b)
                    break

                if curr_vec == 'R':
                    curr_x += 1
                elif curr_vec == 'L':
                    curr_x -= 1
                elif curr_vec == 'U':
                    curr_y -= 1
                elif curr_vec == 'D':
                    curr_y += 1

                if (curr_x, curr_y, curr_vec) == (start_x, start_y, start_vec):
                    break

            else:
                b = branch.pop(0)
                done.add(b)
            
            # print(branch)
            # print(done)
        else:
            branch.pop(0)

    # print(len(energised))
    return len(energised)

# print(run(0,0,'R'))
# print(run(78,0,'D'))

#----------PART 2----------#
res_2 = []

for x in range(x_lim):
    # print(x,0,'D')
    res_2.append(run(x,0,'D'))
    # print(x,y_lim - 1,'U')
    res_2.append(run(x,y_lim - 1,'U'))

for y in range(y_lim):
    # print(0,y,'R')
    res_2.append(run(0,y,'R'))
    # print(x_lim-1,y,'L')
    res_2.append(run(x_lim-1,y,'L'))

print(max(res_2))