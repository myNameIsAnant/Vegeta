"""
Question link

https://www.codingninjas.com/studio/problems/k-most-occurrent-numbers_625382
"""

from typing import List


def getFrequencies(v: List[int]) -> List[int]:
    my_dict = {}
    for x in v:
        my_dict[x] = my_dict.get(x, 0) + 1

    # lst_max = [x for x in my_dict if my_dict[x] == max(my_dict.values())]
    # lst_min = [x for x in my_dict if my_dict[x] == min(my_dict.values())]
    # return [min(lst_max), min(lst_min)]
    maxfreq = 0
    minfreq = float("inf")
    maxval = float("inf")
    minval = float("inf")

    for value, freq in my_dict.items():
        if freq > maxfreq or freq == maxfreq and value < maxval:
            maxfreq = freq
            maxval = value
        if freq < minfreq or freq == minfreq and value < minval:
            minfreq = freq
            minval = value

    return [maxval, minval]


if __name__ == "__main__":
    v = [10, 10, 3, 3]
    print(getFrequencies(v))

# ------------------------------------------------------#


# def getFrequencies(v: List[int]) -> List[int]:
#     my_dict = {}
#     for x in v:
#         my_dict[x] = my_dict.get(x, 0) + 1

#     d = dict(sorted(my_dict.items(), key=lambda x: x))
#     maxval = max(d, key=lambda x: d[x])
#     minval = min(d, key=lambda x: d[x])

#     return [maxval, minval]


# if __name__ == "__main__":
#     v = [10, 10, 10, 3, 3, 3]
#     print(getFrequencies(v))
