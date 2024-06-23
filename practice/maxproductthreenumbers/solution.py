from typing import List


def max_product_of_three(numbers: List[int]) -> int:
    sorted_numbers = sorted(numbers)
    left = sorted_numbers[:3:1]
    right = sorted_numbers[-3:]
    a = right[0] * right[1] * right[2]
    b = left[0] * left[1] * right[2]
    return max([a, b])
