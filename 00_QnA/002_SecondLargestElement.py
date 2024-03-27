"""
Naukri Code 360: Second Largest Number
https://www.naukri.com/code360/problems/ninja-and-the-second-order-elements_6581960
"""

from typing import List


def getSecondOrderElements(n: int, a: List[int]) -> List[int]:
    lrg = seclrg = float("-inf")
    sml = secsml = float("inf")
    for i in range(n):
        if a[i] < sml:
            secsml = sml
            sml = a[i]
        elif a[i] < secsml and a[i] != sml:
            secsml = a[i]

        if a[i] > lrg:
            seclrg = lrg
            lrg = a[i]
        elif a[i] > seclrg and a[i] != lrg:
            seclrg = a[i]
    return [seclrg, secsml]


print(getSecondOrderElements(4, [3, 4, 5, 2]))
