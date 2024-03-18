from typing import List


def mergeSort(array: List[int]) -> List:
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    return startMerge(left_half, right_half)


def startMerge(left_half: List[int], right_half: List[int]) -> List[int]:
    result = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    while i < len(left_half):
        result.append(left_half[i])
        i += 1

    while j < len(right_half):
        result.append(right_half[j])
        j += 1

    return result


my_array = [1, 3, 6, 7, 1, 2, 4, 3, 4, 5]
print(mergeSort(my_array))
