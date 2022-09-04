#take input from the user
encryptthis = input('Enter the string you want to encrypt: ')
#take shift value from the user 1 to 25

numbers = list(range(0,11))
number = str(numbers)
print(type(number))
shift = input('Enter a shift value from 1-25: ')
if shift.isdigit():
    # preserv the lower case and non alphabet characters
    shift = int(shift)
    if shift >= 1 and shift <= 25:
        cipher = ''
        nums = ''
        for letter in encryptthis:
            if letter == ' ':
                cipher = cipher + " "
            elif letter in number:
                cipher = cipher + letter
            elif letter.islower() and (ord(letter) + shift > ord('z')):
                n = ord('z') - ord(letter)
                nn = shift - n
                code = ord('a')-1 + nn
                cipher = cipher + chr(code)
            elif letter.islower() and (ord(letter) + shift <= ord('z')):
                code = ord(letter) + shift
                cipher = cipher + chr(code)
            elif letter.isupper() and (ord(letter) + shift > ord('Z')):
                n = ord('Z') - ord(letter)
                nn = shift - n
                code = ord('A')-1 + nn
                cipher = cipher + chr(code)
            elif letter.isupper() and (ord(letter) + shift <= ord('Z')):
                code = ord(letter) + shift
                cipher = cipher + chr(code)
        print(cipher)



else:
    print('The shift value is not a number!')




