from typing import List


def setpivot(array: List[int], low, high):
    pivot = array[low]
    i = low
    j = high

    while i < j:
        while array[i] <= pivot and i <= high - 1:
            i += 1
        while array[j] > pivot and j > low + 1:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]

    array[low], array[j] = array[j], array[low]
    return j


def quickSort(array: List[int], low, high):
    if low < high:
        pvtind = setpivot(array, low, high)
        quickSort(array, low, pvtind - 1)
        quickSort(array, pvtind + 1, high)


array = [64, 34, 25, 12, 22, 12, 12, 11, 90]
quickSort(array, 0, len(array) - 1)
print(array)
