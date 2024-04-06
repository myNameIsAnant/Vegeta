"""
Naukri Code 360: Find Nth Root Of M
https://www.naukri.com/code360/problems/nth-root-of-m_1062679
"""


def NthRoot(n: int, m: int) -> int:
    low = 1
    high = m // n + 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if mid**n == m:
            return mid
        elif mid**n > m:
            high = mid - 1
        else:
            low = mid + 1
    return -1


n = 9
m = 262144
print(NthRoot(n, m))
