"""
Naukri Code 360: Two Sum
https://www.naukri.com/code360/problems/two-sum_6845742
"""

from typing import List


def read(n: int, book: List[int], target: int) -> str:
    num_map = {}
    for x in range(n):
        rem = target - book[x]
        if rem in num_map:
            return "YES"
        num_map[book[x]] = x

    return "NO"
