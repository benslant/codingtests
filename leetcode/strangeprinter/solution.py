from typing import Dict, List


class Solution:
    def strangePrinter(self, s: str) -> int:
        s_lower = s.lower()
        chunks: Dict[str, List[List[int, int]]] = {}
        current_char = s[0]
        count = 0
        chunks[current_char] = [[0, count]] 
        for i, c in enumerate(s_lower):
            if i == (len(s_lower)-1):
                if c != current_char:
                   chunks[c] = [i, 1]
                else:
                   chunks[current_char][1] = count 
            if c != current_char:   
                    chunks[current_char][1] = count
                    current_char = c
                    count = 1
                    chunks[current_char] = [i, count]
            else:
                count += 1
        return len(chunks)
