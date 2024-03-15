parse = []
res = 0

with open(r'day2.txt', 'r') as f:
    file = f.readlines()
    game_id = 1

    for i in file:
        line = i.strip() + ';'
        game = []
        flag = True
        colors = [0,0,0]  # [r,g,b]
        for g in range(len(line)):
            if line[g] == ';':         
                n = 1
                while True:
                    if line[g-n] in [':', ';']:
                        break
                    else:
                        n += 1
                round = line[g-n+2:g]
                # print(round)
                for r in range(len(round)):
                    if round[r:r+3] == 'red':
                        n = 1
                        while True:
                            if round[r-n-1:r-1].isdecimal():
                                n += 1
                            else:
                                break
                        n_red = int(round[r-n:r-1])
                        if n_red > colors[0]:
                            colors[0] = n_red

                    if round[r:r+3] == 'gre':
                        n = 1
                        while True:
                            if round[r-n-1:r-1].isdecimal():
                                n += 1
                            else:
                                break
                        colors[1] = int(round[r-n:r-1]) if int(round[r-n:r-1]) > colors[1] else colors[1]
                    if round[r:r+3] == 'blu':
                        n = 1
                        while True:
                            if round[r-n-1:r-1].isdecimal():
                                n += 1
                            else:
                                break
                        colors[2] = int(round[r-n:r-1]) if int(round[r-n:r-1]) > colors[2] else colors[2]
        res = 1
        for i in colors:
            res *= i

        parse.append(res)
        # if flag:
        #     res += game_id

        # parse.append(game)
        game_id += 1

print(sum(parse))

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green