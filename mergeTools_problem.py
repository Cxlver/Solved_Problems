
def merge_the_tools(string, k):

    subStr = len(string) // k
    oldStr = ""

    for n in range(len(string)):
        if n % subStr == 0:
            oldStr += '\n' + string[n]
        else:
            oldStr += string[n]

    splitString = oldStr.strip().split('\n')
    uniqChars_arr = []

    for i in range(len(splitString)):
        for l in splitString[i]:
            if l not in uniqChars_arr:
                uniqChars_arr.append(l)

    uniqChars = ''.join(uniqChars_arr)
    newStr = ""

    for item in range(len(uniqChars)):
        if item % subStr == 0:
            newStr += '\n' + uniqChars[item]
        else:
            newStr += uniqChars[item]

    print(newStr.lstrip())

def main():
    string = input().lstrip()
    print(f"The length of the string is {len(string)} characters")

    k = int(input())
    merge_the_tools(string, k)


if __name__ == '__main__':
    main()