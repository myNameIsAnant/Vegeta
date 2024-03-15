from typing import List


def bubbleSort(array: List[int]):
    n = len(array)
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


array = [55, 32, 65, 75, 34]
bubbleSort(array)
print(array)

array = [13, 46, 24, 52, 20, 9]
bubbleSort(array)
print(array)
