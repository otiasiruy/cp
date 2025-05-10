from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        def comb(arr, index):
            if len(arr) > 3:
                return
            if len(arr) == 3:
                subs.append(arr[:])
                return
            for i in range(index, n):
                arr.append(digits[i])
                comb(arr, i + 1)
                arr.pop()
            return

        def backtracking(sub, id):
            x = int(''.join(map(str, sub)))
            if x > 99 and id == len(sub) and x % 2 == 0 and x not in seen:
                ans.append(x)
                seen.add(x)
                return
            for i in range(id, len(sub)):
                a = sub[i]
                sub[i] = sub[id]
                sub[id] = a
                backtracking(sub, id + 1)
                a = sub[i]
                sub[i] = sub[id]
                sub[id] = a

        n = len(digits)
        ans = []
        seen = set()
        memo = set()
        subs = []
        comb([], 0)
        for sub in subs:
            if tuple(sub) not in memo:
                memo.add(tuple(sub))
                backtracking(sub, 0)
        ans.sort()
        return ans