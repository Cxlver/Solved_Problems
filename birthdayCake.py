
def birthdayCakeCandles(ar):

    count_c = 0

    for n in range(ar_count):
        if ar[n] == max(ar):
            count_c += 1
        else:
            count_c += 0

    return count_c

if __name__ == '__main__':

    ar_count = int(input('Enter the amount of candles: '))

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
    print(result)
