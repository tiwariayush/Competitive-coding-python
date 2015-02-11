Q = int(raw_input())

import json

json_data = []
for l in range(Q):
    json_data.append(raw_input())

D = int(raw_input())

dup_data = []
for l in range(D):
    dup = raw_input().split()
    dup_data.append(dup)

N = int(raw_data())

test_dup_data = []
for l in range(N):
    test_dup = raw_input.split()
    m = 0
    n = 0
    for x in dup_data:
        if test_dup[0] in x:
            m = int(x[2])
        if test_dup[1] in x:
            n = int(x[2])
    p = m*n
    print '%s %s %s'test_dup[0],test_dup[1], p
