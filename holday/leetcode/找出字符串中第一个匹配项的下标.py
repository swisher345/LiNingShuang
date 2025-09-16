class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = needle
        h = haystack
        if len(n) > len(h):
            return -1
        if n in h :
            for i in range(len(h)-len(n)+1) :
                if h[i:i+len(n)] == n:
                    return i
        if n not in h:
            return -1
res = Solution()
print(res.strStr("hello","ll"))