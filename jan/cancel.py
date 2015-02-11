data = []
for l in range(int(raw_input())):
    case = []
    x = raw_input().split()
    n = int(x[0])
    k = int(x[1])
    time = [int(l) for l in raw_input().split()]
    case.append(n)
    case.append(k)
    case.append(time)
    data.append(case)

for l in data:
    cancel = 'YES'
    gre = len(filter(lambda x: x<=0, l[2]))
#    import pdb; pdb.set_trace()
    if gre>=l[1]:
        cancel = 'NO'
    print cancel
