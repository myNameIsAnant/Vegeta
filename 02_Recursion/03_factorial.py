def calculateFactorial(num: int) -> int:
    if num == 1 or num == 0:
        return 1
    return num * calculateFactorial(num - 1)


print(calculateFactorial(5))
