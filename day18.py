
#----------PART 1----------#
path = []
with open(r'day18.txt', 'r') as f:
    file = f.readlines()   
    for i in file:
        d, n, hex = i.split()
        path.append((d, int(n), hex[2:-1])) 

print(path)
    
#----------PART 2----------#
