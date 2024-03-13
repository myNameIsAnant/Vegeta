def sumDigits(num: int) -> int:
    if num == 1:
        return 1
    return num + sumDigits(num - 1)


if __name__ == "__main__":
    print(sumDigits(25))
