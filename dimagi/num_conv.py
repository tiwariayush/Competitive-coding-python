N = int(raw_input())

# Listing the complete changes for number upto 19

till19 = ['zero', 'one', 'two', 'three', 'four','five',
          'six', 'seven', 'eight', 'nine', 'ten',
          'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
          'sixteen', 'seventeen', 'eighteen', 'nineteen']

# Listing the converters in tens for number between 20 and 100

tens_conv = ['twenty', 'thirty', 'forty', 'fifty',
             'sixty', 'seventy', 'eighty', 'ninety']

# Listing converters for numbers above 100

large_conv = ['', 'thousand', 'million', 'billion','trillion',
              'quadrillion', 'quintillion', 'sextillion','septillion']

# Function to convert to words

def convert_under20(num):
        return till19[num]

def convert_under100(num):
    if num%10==0:
        word = tens_conv[(num/10)-2]
    else:
        word  = tens_conv[(num/10)-2] + ' ' +till19[num%10]
    return word

def convert_under1000(num):
    word = ''
    (modulus, rem) = (num%100, num//100)
    if rem > 0:
        word  = till19[rem] +' hundred'
        if modulus==0: return word
        if modulus > 0 and modulus>=20:
            word = word +' ' + convert_under100(modulus)
        else:
            word  =word +' '+ convert_under20(modulus)
    return word

def convert_to_word(num):
    if num<20:
        return convert_under20(num)
    elif num<100:
        return convert_under100(num)
    elif num<1000:
        return convert_under1000(num)
    else:         
        for (x, val) in ((v-1, 1000**v) for v in range(len(large_conv))):
            if val > num:
                mod = 1000**x
                l = num//mod
                r = num-(l*mod)
                if l<20:
                    word_new = convert_under20(l)+' '+large_conv[x]
                elif l<100:
                    word_new = convert_under100(l)+' '+large_conv[x]
                else:
                    word_new = convert_under1000(l)+' '+large_conv[x]
                if r>0:
                    word_new =  word_new + ', ' + convert_to_word(r)
                return word_new
        
print convert_to_word(N)
