#!usr/bin/python

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(key, string):
    '''
        Function to encrypt string according to
        key given
    '''

    if len(key)>len(string):
        # Taking case where len of key is greater than len of string
        key = key[:len(string)]

    else:
        x = len(string)/len(key)
        # Modifying key length
        key = key*(x+1)
        key = key[:len(string)]

    code = []

    for i in range(len(string)):
        # Finding index for each character
        z = alphabets.index(key[i])+alphabets.index(string[i])
        if z>25:
            z = z-26
        code.append(alphabets[z])

    return ''.join(code)

def decrypt(key, string):
    '''
        Function to decrypt string according to
        key given
    '''

    if len(key)>len(string):
        # Taking case where len of key is greater than len of string
        key = key[0:len(string)]

    else:
        x = len(string)/len(key)
        # Modifying key length
        key = key*(x+1)
        key = key[:len(string)]

    code = []

    for i in range(len(string)):
        # Finding new index for eaach character
        z = alphabets.index(string[i])-alphabets.index(key[i])
        if z<0:
            z = z+26
        code.append(alphabets[z])

    return ''.join(code)

def main():
    '''
    Main fuction to maintain calls to encrypt and
    decrypt function
    '''
    
    print "Enter the encryption key"
    key = [l.upper() for l in list(raw_input()) if l.strip() and l.isalnum()]

    print "Type E for encryption and D for decryption or B for both simultaneously"
    x = raw_input()

    if x.upper()=="E":
        print "Enter the string to be encrypted"
        string = [l.upper() for l in  list(raw_input()) if l.strip() and l.isalnum()]
        print encrypt(key, string)

    elif x.upper()=="D":
        print "Enter the string to be decrypted"
        string = [l.upper() for l in  list(raw_input()) if l.strip() and l.isalnum()]
        print decrypt(key, string)

    else:
        print "Enter the string"
        string = [l.upper() for l in  list(raw_input()) if l.strip() and l.isalnum()]
        enc = encrypt(key, string)
        print enc
        print decrypt(key, enc)
 
main()
