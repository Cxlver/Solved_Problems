
def breakingRecords(scores):

    '''Given the array, the function prints the amount of time the record has been broken for most and least values.'''

    maxScore = scores[0]
    minScore = scores[0]

    beatMax = 0
    beatMin = 0

    for i in range(n):
        if scores[i] > maxScore:
            maxScore = scores[i]
            beatMax += 1
        elif scores[i] < minScore:
            minScore = scores[i]
            beatMin += 1
        else:
            continue

    return str(beatMax) + ' ' + str(beatMin)

if __name__ == "__main__":

    n = int(input())
    scores = list(map(int, input("Enter some integers: ").rstrip().split()))

    print(breakingRecords(scores))
