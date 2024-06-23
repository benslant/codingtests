import sys
import time
from typing import Dict, List, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result: Dict = {}
        numbers = {i:v for (i, v) in dict(enumerate(nums)).items()}
        l = len(nums)
        lp, rp = 0, l-1
        for lp in range(l):
            sum = 0
            for k in range(rp, 0, 1):
                sum = numbers[i] + numbers[j] + numbers[k]
                if sum == 0: 
                    result[f'{sorted([numbers[i],numbers[j],numbers[k]])}'] = [numbers[i],numbers[j],numbers[k]]
        return list(result.values())

cases: List[Tuple[List, List]] = [([-1,0,1,2,-1,-4,-2,-3,3,0,4],([])),
                                  ([3,-2,1,0], []),
                                  ([-2,0,1,1,2], []),
                                  ([-1,0,1,0], [[-1,0,1]]),
                                  ([-1,0,1,2,-1,-4],[[-1,-1,2],[-1,0,1]]),
                                  ([0,1,1],[]),
                                  ([0,0,0],[]),
                                  ([3,-2,1,0],[])]
# cases: List[Tuple[List, List]] = [([-1,0,1,2,-1,-4],[[-1,-1,2],[-1,0,1]])]

# ([-1,0,1,2,-1,-4],[[-1,-1,2],[-1,0,1]]), ())

# def test():
#     s = Solution()
#     for case in cases:
#         assert s.threeSum(case[0]) == case[1]

# test()

def call(value):
    st = time.time()
    s = Solution()
    result = s.threeSum(value[0])
    mem = sys.getsizeof(s)
    et = time.time()
    print(f'time: {et-st}, memory: {mem} bytes, result:{result}')

def harness(cases):
    [call(c) for c in cases]

harness(cases)