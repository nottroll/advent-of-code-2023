import copy
import math
#----------PART 1----------#

md = {}

conj_mod_state = {}
ff_mod_state = {}

with open(r'day20.txt', 'r') as f:
    file = f.readlines()

    for i in file:
        j = i.split(' -> ')
        if j[0] == 'broadcaster':
            bc = j[1][:-1].split(', ')
        else:
            md[j[0][1:]] = [j[0][0], j[1][:-1].split(', ')]

print(bc,'\n')
# print(md,'\n')

for key in md.keys():
    if md[key][0] == '&':
        for k, v in md.items():
            if key in v[1]:
                if conj_mod_state.get(key):
                    new = dict(conj_mod_state.get(key))
                    new[k] = 0
                    conj_mod_state[key] = new
                else:
                    conj_mod_state[key] = {k:0}
    if md[key][0] == '%':
        ff_mod_state[key] = False

# print(conj_mod_state, '\n')
# print(ff_mod_state, '\n')

blank_conj_state = copy.deepcopy(conj_mod_state)

cnt=0
res_2 = {}

def run():
    global cnt
    cnt += 1
    # print(f'\n-----RUN {cnt}-----')
    global conj_mod_state
    global ff_mod_state
    hi_count, lo_count = 0, 1
    curr_step = [[b, 0] for b in bc]
    # conj_mod_state = copy.deepcopy(blank_conj_state)

    step = 0
    while len(curr_step) > 0:
        step += 1
        next_step = []
        flip_ff_mod_state = set()

        # print('\nSTEP', curr_step)
        for curr_mod, curr_pulse in curr_step:
            if curr_pulse == 0: lo_count += 1
            elif curr_pulse == 1: hi_count += 1

            if md.get(curr_mod):
                for mod_dest in md.get(curr_mod)[1]:
                    # print('   SUBSTEP', curr_pulse, curr_mod, end=' ')

                    if curr_mod in conj_mod_state:  # conj module
                        total_s = sum(list(conj_mod_state[curr_mod].values()))
                        state = list(conj_mod_state[curr_mod].values())
                        if total_s == len(state): next_pulse = 0
                        else: next_pulse = 1
                            
                        if curr_mod in ['tr','xm','dr','nh'] and next_pulse == 1:
                            if res_2.get(curr_mod): pass
                            else: res_2[curr_mod] = cnt, step
                        # if curr_mod == 'dh' and total_s == 1:
                        #     print(cnt)
                        #     print(conj_mod_state.get('dh'))

                            # print(curr_mod, cnt)

                        next_step.append([mod_dest, next_pulse])

                        # if mod_dest in conj_mod_state:
                        #     conj_mod_state[mod_dest][curr_mod] = next_pulse

                    else:  # not conj module
                        if curr_pulse == 0:
                            if ff_mod_state[curr_mod]: next_pulse = 0
                            else: next_pulse = 1
                                
                            flip_ff_mod_state.add(curr_mod)            
                            
                            next_step.append([mod_dest, next_pulse])

                    if mod_dest in conj_mod_state:
                        conj_mod_state[mod_dest][curr_mod] = next_pulse

                    # if next_step:
                    #     print('-',next_step[-1][1],'->', mod_dest)
                    # print('   ',ff_mod_state) 
                    # print('   ',conj_mod_state)
                    # print(conj_mod_state.get('dh'))
                    # print(flip_ff_mod_state)

        for flip in flip_ff_mod_state:
            if ff_mod_state.get(flip) != None:
                ff_mod_state[flip] = not ff_mod_state.get(flip)

        curr_step = next_step

        # cnt += 1
        # if cnt == 10:
        #     break
    # print(hi_count, lo_count)
    # res.append([hi_count, lo_count])
    return hi_count, lo_count

# h_seq, l_seq = 0,0
# for _ in range(2):
#     h, l = run()
#     h_seq += h
#     l_seq += l
# print(h_seq*l_seq)

n = 0
while True:
    run()
    n += 1
    if n == 10000:
        print('hd', conj_mod_state.get('hd'))
        print('tr', conj_mod_state.get('tr'))
        print('dh', conj_mod_state.get('dh'))
        break
print(res_2)
# print(math.lcm(1621,1681,2697,2705))
# print(math.lcm(1655684, 100775))

def n_cycle():
    res = []
    res_set = set()
    max_seq_len = 0
    res_seq = []

    hi_lo = run()
    res.append(hi_lo)
    res_set.add(hi_lo)

    cont = True
    while cont == True:
        hi_lo = run()
        res.append(hi_lo)
        res_set.add(hi_lo)

        if res[-1] in res_set:
            candidate = []
            for i in range(len(res)-1):
                if res[i] == res[-1]:
                    candidate.append(i)

            for idx in candidate:
                shift = 1
                while len(res)-1-shift > idx:
                    # print(idx, len(res_2)-1-shift, res_2[len(res_2)-1-shift],idx-shift, res_2[idx-shift])
                    if res[len(res)-1-shift] != res[idx-shift]:
                        # print('test')
                        break
                    shift += 1
                else:
                    # print(res_2[idx+1:])
                    if len(res[idx+1:]) > 2 and len(res[idx+1:]) > max_seq_len:
                        max_seq_len = len(res[idx+1:])
                        res_seq = idx + 1, len(res) - 1, res[idx+1:]
                        cont = False
                        break
    print('Idx repeat:',res_seq[0], res_seq[1], 'Seq:',res_seq[2])
    return res_seq

# seq = n_cycle()[2]

# h_seq, l_seq = 0,0
# for h, l in seq:
#     h_seq += h
#     l_seq += l
# print(h_seq,l_seq)

# q, r = divmod(1000, len(seq))

# h_rem, l_rem = 0,0
# for i in range(r):
#     h_rem += seq[i][0]
#     l_rem += seq[i][1]

# print(h_seq * q + h_rem, l_seq * q + l_rem)

# print((h_seq * q + h_rem )*(l_seq * q + l_rem))


#----------PART 2----------#
