import string

strlist = list(string.ascii_lowercase)

s = raw_input()

pal = []
for l in strlist:
    pal.append(s.count(l))
    
pal = [l%2 for l in pal]

if pal.count(1)==1:
    print('YES')
elif pal.count(1)==0:
    print('YES')
else:
    print('NO')
