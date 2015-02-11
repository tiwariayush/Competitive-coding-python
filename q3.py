inp = raw_input()

num = [int(l) for l in inp.split()]

N = num[0]
maxdiff = num[1]

digits = len(list(str(N)))

new_conv_digit_list = []

for l in range(digits):
    new_conv_digit_list.append('9')

new_conv_digit = int(''.join(new_conv_digit_list))

d= [l for l in str(N)]

least_num = ['1']
for l in range(digits-1):
    least_num.append('0')

least_num = int(''.join(least_num))

final = []
while(new_conv_digit>least_num):
    p = 0
    for x in range(digits):
        p = p+ abs(int(d[x])-int(new_conv_digit_list[x]))
    if p<=maxdiff:
        final.append(new_conv_digit)
    new_conv_digit = new_conv_digit - 3
    new_conv_digit_list = [l for l in str(new_conv_digit)]

print len(final)
