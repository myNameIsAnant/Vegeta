def reverseNumber(num: int) -> int:
    n = num
    revnum = 0
    while n > 0:
        revnum = (revnum * 10) + (n % 10)
        n = n // 10
    return revnum


print(reverseNumber(1973))
print(reverseNumber(1234))
print(reverseNumber(6786521))
print(reverseNumber(16509))
