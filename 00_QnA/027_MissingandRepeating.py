"""
Naukri Code 360: Missing And Repeating Numbers
https://www.naukri.com/code360/problems/missing-and-repeating-numbers_6828164
"""

from typing import List


def findMissingRepeatingNumbers(a: List[int]) -> List[int]:
    hash_map = {}
    n = len(a)
    sum = dc = me = 0
    for i in a:
        hash_map[i] = hash_map.get(i, 0) + 1
        if hash_map[i] == 1:
            sum += i
        else:
            dc = i
    me = ((n * (n + 1)) // 2) - sum
    return [dc, me]
