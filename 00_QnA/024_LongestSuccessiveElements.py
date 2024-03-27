"""
Naukri Code 360: Longest Successive Elements
https://www.naukri.com/code360/problems/longest-successive-elements_6811740
"""

from typing import List


def longestSuccessiveElements(a: List[int]) -> int:
    ### ***** Method 1 ***** ###
    """
    TC = O(N + n log n) and SC = O(1)
    """
    # a.sort()
    # ct = maxct = 1
    # for i in range(len(a) - 1):
    #     if a[i] + 1 == a[i + 1]:
    #         ct += 1
    #         maxct = max(ct, maxct)
    #     elif a[i] == a[i + 1]:
    #         continue
    #     else:
    #         ct = 1

    # return max(ct, maxct)

    ### ***** Method 2 ***** ###
    """
    TC = O(2N) and SC = O(N)
    """
    hash_map = {}
    ct = max_ct = 0
    for i in range(len(a)):
        hash_map[a[i]] = i
    for k in a:
        while k in hash_map:
            k += 1
            ct += 1
        max_ct = max(max_ct, ct)
        ct = 0
    return max(max_ct, ct)


array = [15, 6, 2, 1, 16, 4, 2, 29, 9, 12, 8, 5, 14, 21, 8, 12, 17, 16, 6, 26, 3]
print(longestSuccessiveElements(array))
