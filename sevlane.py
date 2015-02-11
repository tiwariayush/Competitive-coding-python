X = raw_input().split()

N = int(X[0])
T = int(X[1])

width = [int(l) for l in raw_input().split()]

points = []
for l in range(T):
    points.append(tuple([int(p) for p in raw_input().split()]))

for x in points:
    w = width[x[0]:x[1]+1]
    print min(w)
