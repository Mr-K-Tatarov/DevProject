class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        rtoa={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        for i in range(len(s)-1):
            if (rtoa[s[i]]<rtoa[s[i+1]]):
                res=res-rtoa[s[i]]
            elif (rtoa[s[i]]>=rtoa[s[i+1]]):
                res=res+rtoa[s[i]]

        res=res+rtoa[s[len(s)-1]]

        return res

s = input("Enter roman number: ")
s = s.upper()
obj = Solution()
print(obj.romanToInt(s))