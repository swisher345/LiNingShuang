
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = list(s)
        t1 = list(t)
        print(s1, t1)
        for i in t1:
            print( i)
            if i not in s1:
                return i

res = Solution()
print(res.findTheDifference("a", "aa"))
