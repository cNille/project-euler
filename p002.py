
nbrs = [1,1]
while nbrs[-1] < 4000000: 
    n = nbrs[-1] + nbrs[-2]
    nbrs.append(n)

print('all',nbrs)
even = [ n for n in nbrs if n % 2 == 0]
print('even',even)
print('result', sum(even))

