data = []
for l in range(int(raw_input())):
    x = [int(l) for l in raw_input().split()]
    data.append(x)

for d in data:
    p = range(d[0], d[1]+1)
    print reduce(lambda a,b: a&b,p)
