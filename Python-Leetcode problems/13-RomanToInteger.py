class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {"i" : 1,
                        "v" : 5,
                        "x" : 10,
                        "l" : 50,
                        "c" : 100,
                        "d" : 500,
                        "m" : 1000}
        
        total = 0
        prev = 0
        curr = 0
        
        for i in range(len(s)):
            curr = roman_values[s[i]];
            if curr > prev:
                total = total + curr - prev * 2
            else:
                total += curr
            prev = curr
        return total
            