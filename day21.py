
#----------PART 1----------#
field = []
with open(r'day21.txt', 'r') as f:
    file = f.readlines()
    for i in range(len(file)):
        row = []
        for j in range(len(file[i])-1):
            row.append(file[i][j])
            if file[i][j] == 'S':
                start = j, i 
        field.append(row)
                 
    print(start, field)

class TreeNode:
    def __init__(self, node = None):
        self.node = node
        self.next_node = []

curr_node = TreeNode(start)  # x, y

print(curr_node.node)

for _ in range(1):

    curr_node.node 

#----------PART 2----------#

# r = [1, 2, 3, 3, 3, 2, 1, 1, 2, 2, 3, 3]
# c = [1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 6]
r = [1, 1, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1]
c = [1, 2, 3, 3, 4, 5, 5, 6, 1, 1, 1, 1]
s = set()
h = 5
w = 15

risk = [[4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 2, 0,45, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4,25, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 2, 0]]

p = set(zip(r, c))

for y in range(h):
    for x in range(w):
        if (y + 1, x + 1) in p:
            print('X', end='')
        else:
            print('-', end='')
    print()

for i in range(12):
    # s.append(c[i] * 5 + r[i])

    s.add(min(w,(c[i] + 1)) * h + r[i])
    s.add(max(1,(c[i] - 1)) * h + r[i])
    s.add(c[i] * h + min(h,(r[i] + 1)))
    s.add(c[i] * h + max(1,(r[i] - 1)))

print(s)

tot = 0
for i in s:
    c, r = divmod(i, h)
    tot += risk[r][c]
print(tot)

for i in s:
    q, rem = divmod(i, h)
    print('c=',q,'r=',rem)

t = [[x * (h) + y for x in range(1,w+1)] for y in range(1,h+1)]
print(t)

for i in range(len(t)):
    for j in range(len(t[0])):
        print('c=',divmod(t[i][j], h)[0],'r=',divmod(t[i][j], h)[1])


