import string

def LetterChanges(str):

    vowels = 'aeiou'
    alpha = string.ascii_lowercase
    newString = ''

    for x in str.lower():
        if x not in alpha:
            newChar = x
        else:
            oldPos = alpha.find(x)
            newChar = alpha[(oldPos + 1) % 26]
            if newChar in vowels:
                newChar = alpha[(oldPos + 1) % 26].upper()
            else:
                newChar = alpha[(oldPos + 1) % 26]

        newString += newChar

    return newString

print(LetterChanges(str=input('Enter any string:')))

def SimpleSymbols(str):
    s = '=' + str + '='
    for i in s:
        if i in string.ascii_lowercase:
            if not s[s.index(i) - 1] == '+' or not s[s.index(i) + 1] == '+':
                return 'false'
    return 'true'

# print(SimpleSymbols(str=input('Enter any string: ')))

def AlphabetSoup(str):
    '''Have the function AlphabetSoup(str) take the str string parameter
    being passed and return the string with the letters in alphabetical
    order (ie. hello becomes ehllo). Assume numbers and punctuation symbols
    will not be included in the string. '''

    lst = [x for x in str.lower() if x.isalpha()]

    return ''.join(sorted(lst))

# print(AlphabetSoup(str=input('Enter any string: ')))

