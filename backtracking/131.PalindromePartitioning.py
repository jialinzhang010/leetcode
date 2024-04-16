class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        def helper(i):
            if i == len(s):
                ans.append(path[:])
                return
            for j in range(i, len(s)):
                curr = s[i : j + 1]
                if not self.isP(curr):
                    continue
                path.append(curr)
                helper(j + 1)
                path.pop()
        helper(0)
        return ans
    
    def isP(self, s):
        if len(s) == 1:
            return True
        a = len(s) // 2
        for i in range(a):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True