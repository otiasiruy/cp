from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        def backtrack(curr, id):
            if len(curr) == len(digits):
                ans.append(curr)
                return
            for j in range(len(nl[int(digits[id]) - 2])):
                curr = "".join([curr, nl[int(digits[id]) - 2][j]])
                backtrack(curr, id + 1)
                curr = curr[:-1]

        nl = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
              ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        ans = []
        backtrack("", 0)
        return ans
