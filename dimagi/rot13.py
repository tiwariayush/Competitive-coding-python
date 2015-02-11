n = raw_input()

def rot13(s):
    result = ""

    for l in s:
        c = ord(l)

        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13

        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13

        result += chr(c)
    result = result[::-1]
    return result

print(rot13(n))
print(rot13(rot13(n)))
