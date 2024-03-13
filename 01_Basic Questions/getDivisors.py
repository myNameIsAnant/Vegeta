def getFactors(num: int) -> list:
    factor_list = []
    for x in range(1, (int(num**0.5)) + 1):
        if num % x == 0:
            factor_list.append(x)
            if x != num // x:
                factor_list.append(num // x)
    factor_list.sort()
    return factor_list


if __name__ == "__main__":
    print(getFactors(120))
