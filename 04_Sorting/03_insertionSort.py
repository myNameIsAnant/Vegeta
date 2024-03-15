from typing import List


def insertionSort(array: List[int]):
    n = len(array)
    for i in range(1, n):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


array = [14, 9, 15, 12, 6, 8, 13]
insertionSort(array)
print(array)
