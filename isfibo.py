import math
T = int(raw_input())

num = []
for x in range(T):
    num.append(int(raw_input()))

def isfibo(n):
    if n>=0:
        return math.sqrt(5*n*n-4).is_integer() or math.sqrt(5*n*n+4).is_integer()

for n in num:
    if isfibo(n):
        print "IsFibo"
    else:
        print "IsNotFibo"
    
