
def divisibleSumPairs(n, k, ar):

    count = 0
    for i in range(n):
        for j in range(n):
            if (ar[i] + ar[j]) % k == 0 and i < j:
                count += 1

    return f"Count of pairs : {count}"

if __name__ == '__main__':

    nk = input().split() # 2 integers separated by space

    n = int(nk[0]) # Integer length of the ar

    k = int(nk[1]) # Number the sum should be divisible by

    ar = list(map(int, input().rstrip().split())) # Array of integers

    result = divisibleSumPairs(n, k, ar)
    print(result)