"""
Naukri Code 360: Superior Elements
https://www.naukri.com/code360/problems/superior-elements_6783446
"""

from typing import List


def superiorElements(a: List[int]) -> List[int]:
    result = [a[-1]]
    maxel = a[-1]
    r = len(a) - 2
    while r >= 0:
        if a[r] > maxel:
            result.append(a[r])
            maxel = a[r]
        r -= 1
    return result


array = [1, 2, 3, 2]
print(superiorElements(array))
