num = []
for l in range(int(raw_input())):
    num.append(int(raw_input()))
            
for n in num:
    n3 = 0
    n5 = 0
    numdict = []
    if n<3:
        print -1
    else:
        while(n3<=n and n5<=n):
            if n>0:
                n3 = n3+1
                n5 = n-n3
            if n3%5==0 and n5%3==0:
                numdict.append((n5, n3))
                
                if len(numdict)>1:
                    for x in numdict:
                        if x[0]>=x[1]:
                             print x
        print numdict
        
                                  
