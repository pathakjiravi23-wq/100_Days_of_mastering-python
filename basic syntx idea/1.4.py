def nSum(n):
    ans = 0
    for i in range(1, n + 1):
        ans = ans + i
    return ans


def prunt():
    x = int(input("enter"))
    y = nSum(x)
    print(y)
