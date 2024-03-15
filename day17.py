
#----------PART 1----------#

with open(r'day17.txt', 'r') as f:
    file = f.readlines()
    field = [[int(i[j]) for j in range(len(i)-1)] for i in file]

print(field)



#----------PART 2----------#
