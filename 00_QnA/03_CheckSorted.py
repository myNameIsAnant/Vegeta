"""

"""

from typing import List


def isSorted(n: int, a: List[int]) -> int:
    for i in range(n - 1):
        if a[i + 1] < a[i]:
            return 0
    return 1


print(isSorted(5, [1, 2, 3, 4, 5]))