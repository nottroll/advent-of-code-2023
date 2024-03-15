
import itertools

#----------PART 1----------#
record = []
pattern = []

with open(r'day12.txt', 'r') as f:
    file = f.readlines()
    for line in file:
        s, p = line.split()
        record.append(s)
        # record.append([s[i] for i in range(len(s))])
        pattern.append([int(i) for i in p.split(',')])

def add(n, value):
    arr = [0]*n
    sumRecursive(n, value, 0, n, arr)

fill_gaps = []

# def sumRecursive(n, value, sumSoFar, topLevel, arr):
#     global fill_gaps
#     if n == 1:
#         if sumSoFar <= value:
#             if topLevel == 1 or (value - sumSoFar >= arr[-2]):
#                 arr[(-1)] = value - sumSoFar
#                 # fill_gaps += [list(arr)]
#                 print(arr)

#     elif n > 0:
#         start = 0
#         if (n != topLevel):
#             start = arr[(-1*n)-1]

#         for i in range(start, value+1):
#             # print((-1*n), i)
#             arr[(-1*n)] = i 
#             sumRecursive(n-1, value, sumSoFar + i, topLevel, arr)

def add(n, value):
    arr = [0]*n
    memo = {}
    sumRecursive(n, value, 0, n, arr, memo)

def sumRecursive(n, value, sumSoFar, topLevel, arr, memo):
    global fill_gaps
    if (n, value, sumSoFar) in memo:
        return memo[(n, value, sumSoFar)]
        
    if n == 1:
        if sumSoFar <= value and (topLevel == 1 or value - sumSoFar >= arr[-2]):
            arr[-1] = value - sumSoFar
            fill_gaps += [list(arr)]
            # print(arr)
            return

    if n > 0:
        start = arr[-n-1] if n != topLevel else 0
        for i in range(start, value+1):
            arr[-n] = i 
            sumRecursive(n-1, value, sumSoFar + i, topLevel, arr, memo)
            
    memo[(n, value, sumSoFar)] = arr

res = []

# for idx in range(len(record)):
#     # print(record[idx])
#     # print(pattern[idx])
#     add(len(pattern[idx])+1, len(record[idx]) - sum(pattern[idx]))
#     # print(fill_gaps)

#     fill_gaps_perm = []

#     for i in fill_gaps:
#         p = itertools.permutations(i)
#         for j in p:
#             fill_gaps_perm.append(j)

#     # print(set(fill_gaps_perm))

#     filter_gap_perm = []

#     for i in set(fill_gaps_perm):
#         # print(i[1:-1])
#         for j in i[1:-1]:
#             if j == 0:
#                 break
#         else:
#             filter_gap_perm.append(i)

#     # print(filter_gap_perm)

#     solns = []
#     for i in filter_gap_perm:
#         s = ''
#         for j in range(len(i) - 1):
#             s += ('.' * i[j]) + ('#' * pattern[idx][j]) 
#         s += ('.' * i[-1])
#         # print(s)
#         solns.append(s)

#     # print(solns)

#     filter_soln = []

#     for soln in solns:
#         for i in range(len(soln)):
#             # print(record[idx][i], soln[i])
#             if record[idx][i] != '?':
#                 if soln[i] != record[idx][i]:
#                     break
#         else:
#             filter_soln.append(soln)

#     res.append(len(filter_soln))
#     # print(len(filter_soln))
#     fill_gaps = []

# print(sum(res))

#----------PART 2----------#

record = [i + ('?' + i) * 4 for i in record]
pattern = [i * 5 for i in pattern]
# print(record, pattern)

for idx in range(1):  # len(record)
    print(record[idx])
    print(pattern[idx])
    add(len(pattern[idx])+1, len(record[idx]) - sum(pattern[idx]))
    print(fill_gaps)

    fill_gaps_perm = []

    for i in fill_gaps:
        p = itertools.permutations(i)
        for j in p:
            fill_gaps_perm.append(j)

    # print(set(fill_gaps_perm))

    filter_gap_perm = []

    for i in set(fill_gaps_perm):
        # print(i[1:-1])
        for j in i[1:-1]:
            if j == 0:
                break
        else:
            filter_gap_perm.append(i)

    # print(filter_gap_perm)

    solns = []
    for i in filter_gap_perm:
        s = ''
        for j in range(len(i) - 1):
            s += ('.' * i[j]) + ('#' * pattern[idx][j]) 
        s += ('.' * i[-1])
        # print(s)
        solns.append(s)

    # print(solns)

    filter_soln = []

    for soln in solns:
        for i in range(len(soln)):
            # print(record[idx][i], soln[i])
            if record[idx][i] != '?':
                if soln[i] != record[idx][i]:
                    break
        else:
            filter_soln.append(soln)

    res.append(len(filter_soln))
    # print(len(filter_soln))
    fill_gaps = []

print(sum(res))