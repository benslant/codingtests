import sys
import time
import pytest

class Solution:
    def intToRomanFast(self, num: int) -> str:
        def choose_int(int_list, x):
            res = int_list[0]
            for k in int_list:
                if k <= x:
                    res = k
                else:
                    break
            return res
            
        roman = ""
        int2rom = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M',}
        int_cand = list(int2rom.keys())
        int_cand.sort()
        while num > 0:
            cur = choose_int(int_cand, num)
            roman += int2rom[cur]
            num -= cur

        return roman

    def intToRoman(self, num: int) -> str:
        result = ''
        m = num // 1000
        c = (num - m*1000) // 100
        x = (num - m*1000 - c*100)// 10
        v = (num - m*1000 - c*100 - x*10)// 5
        if m > 0:
            result+=f"{'M'*m}"
            num -= m*1000
        if c > 0:
            if c == 4: 
                result+="CD"
                num -= c*100
            elif c == 9: 
                result+="CM"
                num -= c*100
            elif (c*100 == 500) or (c*100 - 500 > 0):
                result += 'D'
                num -= 500
                a = num//100
                num -= a*100
                result += f'{"C"*a}'
            else: 
                result+=f"{'C'*c}"
                num -= c*100
        if x > 0:
            if x*10 == 90: 
                result += 'XC'
                num -= x*10
            elif x*10 == 40:
                result +=  'XL'
                num -= x*10
            elif (x*10 == 50) or (x*10 - 50 > 0): 
                result += 'L'
                num -= 50
                a = num//10
                num -= a*10
                result += f'{"X"*a}'
            else: 
                result += f"{'X'*x}"
                num -= x*10
        if v> 0:
            if num == 9: 
                result += 'IX'
                num = 0
            elif (num == 5) or (num - v*5 > 0): 
                result += 'V'
                num -= v*5
            
        l = f"{'I'*num}" if num!=4 else "IV"
        result += l
        
        return result        
        

def call(value):
    st = time.time()
    s = Solution()
    result = s.intToRomanFast(value)
    mem = sys.getsizeof(s)
    et = time.time()
    print(f'time: {et-st}, memory: {mem} bytes, result:{result}')

test = [2000, 600, 200, 60, 20, 8, 6, 9, 3, 58, 1994]
# test = [1994]

def harness(cases):
    [call(c) for c in cases]

harness(test)