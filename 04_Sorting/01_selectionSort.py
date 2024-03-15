from typing import List


def selectionSort(array: List[int]):
    n = len(array)
    for i in range(n):
        minind = i
        for j in range(i + 1, n):
            if array[j] < array[minind]:
                minind = j
        array[i], array[minind] = array[minind], array[i]


array = [64, 25, 12, 22, 11]
selectionSort(array)
print(array)
