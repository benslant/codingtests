from typing import List, Tuple

def find_peak(trend_data: List[int]) -> List[int]:
    if not trend_data: return []
    result: List[int] = []
    for index, point in enumerate(trend_data):
        left, right = 0, 0
        if index > 0: left = trend_data[index - 1]
        if index < (len(trend_data)-1): right = trend_data[index + 1]

        if point > left and point > right:
            result.append(point)

    return result

def find_peaks_and_troughs(trend_data: List[int]) -> List[Tuple[int, int]]:
    if not trend_data: return []
    highest: Tuple[int, int] = (0, 0)
    lowest: Tuple[int, int] = (0, 0)
    for index, point in enumerate(trend_data):
        left, right = 0, 0
        if index > 0: left = trend_data[index - 1]
        if index < (len(trend_data)-1): right = trend_data[index + 1]

        if point > left and point > right:
            if point > highest[0]: highest = (point, index) 

        if point < left and point < right:
            if point < highest[0]: lowest = (point, index) 

    return [highest, lowest]


result = find_peaks_and_troughs([0,4,2,9,2,3,5,0])
print(result)

result = find_peak([0,4,2,9,2,3,5,0])
print(result)


