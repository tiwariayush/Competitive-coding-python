num = []
for l in range(int(raw_input())):
    num.append(int(raw_input()))

for n in num:
    strings = list(str(n))
    final = 0
    for l in strings:
        if not int(l)==0:
            if n%int(l)==0:
                final = final+1
    print final
            
