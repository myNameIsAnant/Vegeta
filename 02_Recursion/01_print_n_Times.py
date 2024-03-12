"""
Print Name 5 Times using Recursion
"""


def printName(count: int, times: int) -> None:
    if count > times:
        return
    print("Anant")
    printName(count + 1, times)


i = 1
n = 5
printName(i, n)
