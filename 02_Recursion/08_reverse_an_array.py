from typing import List


def revArray(array: List, i) -> List:
    if i >= len(array) // 2:
        return array
    array[i], array[len(array) - 1 - i] = array[len(array) - 1 - i], array[i]
    return revArray(array, i + 1)


if __name__ == "__main__":
    array = [3, 5, 1, 7, 8, 6, 5, 100]
    print(revArray(array, 0))
