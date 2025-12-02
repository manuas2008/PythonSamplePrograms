class Solution(object):
    def romanToInt(self, s):
        roman = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        result = 0
        for curr, next in zip(s, s[1:]):
            # print(curr, next)
            if roman[next] <= roman[curr]:
                result += roman[curr]
            else:
                result -= roman[curr]
        return result + roman[s[-1]]

s = Solution()
print(s.romanToInt("LVIII"))
print(s.romanToInt("XCIX"))

