t = int(raw_input())
all_data = []
for l in range(t):
    x = raw_input().split()
    n = int(x[0])
    m = int(x[1])
    arr = [int(p) for p in raw_input().split()]
    data =[]
    data.append(n)
    data.append(m)
    data.append(arr)
    all_data.append(data)

for d in all_data:
    modu = 0
    arr = d[2]
    m = d[1]
    n = d[0]
    arr = sorted(arr, rever)
    for p in xrange(n):
        for q in xrange(p, n):
            new_arr =  arr[p:q+1]
            new_sum = sum(new_arr)
            modu1 = new_sum%m
            if modu1>=modu:
                modu=modu1
            if modu1==(m-1):
                break

    print modu
