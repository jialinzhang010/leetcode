class Solution:
    def countSubstrings(self, s: str) -> str:
        def expand(i, j):
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                count += 1
            return count
        ans = 0
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            ans += odd + even
        return ans