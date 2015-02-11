arr = []

for n in range(int(raw_input())):
    l = int(raw_input())
    p = [int(l) for l in raw_input().split()]
    x = (l, p)
    arr.append(x)

for x in arr:
    i = 0
    lhs = 0
    rhs = sum(x[1])-x[1][0]
    val = [(lhs, rhs)]
    while(rhs>0):
        lhs=lhs+x[1][i]
        rhs=rhs-x[1][i+1]
        i = i+1
        val.append((lhs, rhs))
    final = []
    for l in val:
        if l[0]==l[1]:
            final.append('YES')
        else:
            final.append('NO')
    print next((x for x in final if x!='NO'), 'NO')
