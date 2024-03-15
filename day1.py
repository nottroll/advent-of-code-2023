# res = 0

# with open(r'day1.txt', 'r') as f:
    
#     s = f.readlines()
#     print(s)

#     for i in s:
#         num = ''
#         line = i.strip()
#         for j in range(len(line)):
#             if line[j].isdecimal():
#                 num += line[j]
#         res += int(num[0] + num[-1])


# print(res)

d = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

res = 0
num_1, num_2 = 0, 0
with open(r'day1.txt', 'r') as f:
    
    s = f.readlines()
    # print(s)

    # for _ in range(1):
    for i in s:
        # line = '7rkscrcchttwoggxktqdptwodpkcsgpbseven'
        line = i.strip()
        print(line)
        for j in range(len(line)):
            if line[j] in ('o','t','s'):
                if line[j:j+3] in d:
                    num_1 = d.get(line[j:j+3])
                    break
            if line[j] in ('f','n'):
                if line[j:j+4] in d:
                    num_1 = d.get(line[j:j+4])
                    break
            if line[j] in ('t','s','e'):
                if line[j:j+5] in d:
                    num_1 = d.get(line[j:j+5])
                    break
            if line[j].isdecimal():
                num_1 = int(line[j])
                break
        # print(num_1)

        for j in reversed(range(len(line))):
            if line[j] in ('e','o','x'):
                if line[j-2:j+1] in d:
                    num_2 = d.get(line[j-2:j+1])
                    break
            if line[j] in ('e','r'):
                if line[j-3:j+1] in d:
                    num_2 = d.get(line[j-3:j+1])
                    break
            if line[j] in ('e','n','t'):
                if line[j-4:j+1] in d:
                    num_2 = d.get(line[j-4:j+1])
                    break
            if line[j].isdecimal():
                num_2 = int(line[j])
                break
        res += int(num_1*10 + num_2)
        print(num_1,num_2,int(num_1*10 + num_2))

print(res)