def calculatePower(base, exponent):
    if type(exponent) != int or exponent < 0:
        raise Exception("Invalid Exponent Error")
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    return base * calculatePower(base, exponent - 1)


if __name__ == "__main__":
    print(calculatePower(2, -3))
