N = int(input())

count = 0

while(N>0):
    if not '7' in [x for x in str(N)]:
        count = count+1
    N = N-1
print count
