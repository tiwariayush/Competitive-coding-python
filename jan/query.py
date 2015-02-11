n = int(raw_input())

arr = [int(l) for l in raw_input().split()]

q = int(raw_input())

que = [int(l) for l in raw_input().split()]

for l in que:
    arr = [p+l for p in arr]
    print sum([abs(x) for x in arr])
