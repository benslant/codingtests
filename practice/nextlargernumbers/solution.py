from typing import List


def next_larger_number(circular_array: List[int]) -> List[int]:
    result: List[int] = []
    for i, number in enumerate(circular_array):
        left = i - 1 if i - 1 >= 0 else len(circular_array) - 1
        right = i + 1 if i + 1 < len(circular_array) else 0
        m = max(circular_array[left], circular_array[right])
        ln = m if m > circular_array[i] else -1
        result.append(ln)
    return result
