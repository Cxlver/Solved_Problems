
def longestWord(sen):

    words = "".join(c if c.isalnum() else ',' for c in sen).split(",")
    words_len = set([len(x) for x in words])
    max_len = max(words_len)

    result = [y for y in words if len(y) == max_len][0]

    return result

def main():
    print(longestWord(input("Enter any sentence: ")))

if __name__ == '__main__':
    main()