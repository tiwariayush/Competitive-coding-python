x = raw_input().split()

a = int(x[0])
b = int(x[1])

def rep_square_helper(x, times, res):
    if times == 1:
        return res * x
    if times % 2:
        return rep_square_helper(x * x, times // 2, res * x)
    else:
        return rep_square_helper(x * x, times // 2, res)

def rep_square(n, times):
    return rep_square_helper(n, times, 1)

c = rep_square(2, a)

def power(g_base,a,p_mod):
  x=1
  bits = "{0:b}".format(a)
  for i, bit in enumerate(bits):
    if bit=='1': x = (((x**2)*g_base)%p_mod)
    elif bit=='0': x = ((x**2)%p_mod)
  return x%p_mod

def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number
print power(2, c, b)
