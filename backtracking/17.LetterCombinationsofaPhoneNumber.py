class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {"2":"abc", "3":"def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        inputs = []
        for i in digits:
            inputs.append(hashmap[i])
        ans = []
        path = []
        def helper(i):
            if len(path) == len(digits):
                ans.append("".join(path[:]))
                return
            for j in range(len(inputs[i])):
                path.append(inputs[i][j])
                helper(i + 1)
                path.pop()
        helper(0)
        return ans