"""
Question link

https://www.codingninjas.com/studio/problems/k-most-occurrent-numbers_625382
"""

from typing import List


def getFrequencies(v: List[int]) -> List[int]:
    my_dict = {}
    for x in v:
        my_dict[x] = my_dict.get(x, 0) + 1

    maxfreq = 0
    minfreq = maxval = minval = float("inf")

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
