from typing import List, Tuple

def min_taps_to_water_garden(tap_range: List[int]):
    coverage: List[Tuple[int, int, int]] = []
    for i in range(0, len(tap_range)):
        tap_coverage = (i, i-tap_range[i], i+tap_range[i])
        if tap_coverage[1] == tap_coverage[2]: continue
        if tap_coverage[1] <=0 and tap_coverage[2] >= (len(tap_range)-1):
            return i
        coverage.append(tap_coverage)
    print(coverage)

    

test_range_1 = [3,4,1,1,0,0]
test_range_2 = [3,0,1,1,0,0]

min_taps_to_water_garden(test_range_2)
