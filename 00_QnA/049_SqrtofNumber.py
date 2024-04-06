"""
Naukri Code 360: Square Root of a number
Square Root of a number
"""


def floorSqrt(n):
    low = 1
    high = (n // 2) + 1
    ans = 0
    while low <= high:
        mid = low + ((high - low) // 2)
        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


n = 77
print(floorSqrt(n))
