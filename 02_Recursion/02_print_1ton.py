"""
Print 1 to N using Recursion
"""

# def printNumbers(count: int, times: int) -> None:
#     if count > times:
#         return
#     print(count)
#     printNumbers(count + 1, times)


# if __name__ == "__main__":
#     i = 1
#     n = 5
#     printNumbers(i, n)

"""
Print N to 1 using Recursion
"""


def printNumbers(count: int) -> None:
    if count == 0:
        return
    print(count)
    printNumbers(count - 1)


def printNumbersbt(count: int, num: int) -> None:
    if count > num:
        return
    printNumbersbt(count + 1, num)
    print(count)


if __name__ == "__main__":
    i = 5
    printNumbers(i)
    print("---------")
    i = 1
    printNumbersbt(1, 5)
