import itertools

s1 = str(raw_input())
s2 = str(raw_input())
s3 = str(raw_input())

s1ss = []
for l in range(len(s1)):
    for s in itertools.combinations(s1, l):
        s1ss.append("".join(s))

s2ss = []
for l in range(len(s2)):
    for s in itertools.combinations(s2, l):
        s2ss.append("".join(s))

s4 = list(set(s1ss).intersection(s2ss))

final = []
for l in s4:
    if s3 in l:
        final.append(l)

s5 = list(set(s4)- set(final))

print len(max(s5, key=len))
