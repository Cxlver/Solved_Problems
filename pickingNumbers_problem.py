
def pickingNumbers(a):

    subLst = []

    for i in range(n):
        for l in range(n):
            if abs(a[i] - a[l]) <= 1 and l > i:
                print(f"|{a[i]} - {a[l]}| = {abs(a[i] - a[l])}")
                subLst.append(a[i])
                # for k in range(len(subLst)):
                #     for m in range(len(subLst)):
                #         if abs(subLst[k] - subLst[m]) > 1 and subLst[m] > subLst[k]:
                #             subLst.remove(subLst[m])
    return set(subLst)

if __name__ == '__main__':

    n = int(input().strip())
    if n < 2 or n > 100:
        raise ValueError("'n' input can't exceed 100 and can't be lower than 2")

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(result)