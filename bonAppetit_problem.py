
def bonAppetit(bill, k, charged):

    totalSum = 0

    for i in range(n):
        totalSum += bill[i]

    realCharge = (totalSum - bill[k]) / 2

    if charged == realCharge:
        return "Bon Appetit"
    elif charged < realCharge:
        return "You're too kind!"
    else:
        return int(charged - realCharge)


if __name__ == '__main__':
    nk = input().rstrip().split() # Two spaced integers

    n = int(nk[0]) # Number of items bought

    k = int(nk[1]) # Index of item not needing to be paid

    bill = list(map(int, input().rstrip().split()))

    charged = int(input().strip())

    print(bonAppetit(bill, k, charged))
