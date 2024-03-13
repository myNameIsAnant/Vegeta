"""
Print Name 5 Times using Recursion
"""


def printName(count: int, times: int) -> None:
    if count > times:
        return
    print("Anant")
    printName(count + 1, times)


if __name__ == "__main__":
    i = 1
    n = 5
    printName(i, n)
