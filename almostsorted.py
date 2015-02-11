arr1 = []
n = int(raw_input())

arr1 = [int(l) for l in raw_input().split()]

def presorted(arr):
    if sorted(arr)==arr:
        return True
y = []
def swapsorted(arr):
    for i in range(n):
        for j in range(n):
            new_arr = list(arr)
            new_arr[i], new_arr[j]=new_arr[j], new_arr[i]
            if sorted(arr)==new_arr:
                global y
                y.insert(0,i+1)
                y.insert(1,j+1)
                return y
                break
                

x = []
def reversesorted(arr):
    for i in range(n):
        for j in range(n):
            new_arr = list(arr)
            new_arr[i:j] = new_arr[i:j][::-1]
            if sorted(arr)==new_arr:
                global x
                x.insert(0,i+1)
                x.insert(1, j)
                return x
                break

if presorted(arr1):
    print 'yes'
elif swapsorted(arr1):
    print "yes"
    print "swap %s %s"%tuple(y)
elif reversesorted(arr1):
    print "yes"
    print "reverse %s %s"%tuple(x)
else:
    print 'no'
