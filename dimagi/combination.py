from itertools import product

N = int(raw_input())

lists = []
for l in range(N):
    lists.append(raw_input().split(','))

for l in product(*lists):
    print " ".join(list(l))
