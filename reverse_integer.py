import sys
import time 

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        r_str: str = ''
        if s[0] == '-': 
            r_str = s[0]
            s = s[1:]
        s = int(r_str+s[::-1])
        if s > 2147483647 or s < -2147483647:
            return 0
        return s
    
    def reverse_high_memory(self, x: int) -> int:
        s = str(x)
        r_str: str = ''
        sign = ''
        if s[0] == '-': 
            s = s[1:]
            sign = '-'
        for c in reversed(s):
            r_str += c
        result = int(sign + r_str)
        if result > 2147483647 or result < -2147483647:
            return 0
        return result


test = [123,-123,120, 1534236469]

def call(value):
    st = time.time()
    s = Solution()
    result = s.reverse(value)
    mem = sys.getsizeof(s)
    et = time.time()
    print(f'time: {et-st}, memory: {mem} bytes, result:{result}')

def harness(cases):
    [call(c) for c in cases]

harness(test)

