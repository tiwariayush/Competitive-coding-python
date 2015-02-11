T = int(raw_input())

cycles = []
for x in range(T):
    cycles.append(int(raw_input()))
    
for cycle in cycles:
    c = cycle
    l = 1
    while(c>0):
        l = l*2
        c = c-1
        if c>0:
            l = l+1
            c = c-1
    print l
