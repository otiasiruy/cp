from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        ck = [s[0]]
        for i in range(1, len(s)):
            if i % k != 0:
                ck.append(s[i])
            else:
                ans.append(''.join(ck))
                ck = [s[i]]
        while len(ck) < k:
            ck.append(fill)
        ans.append(''.join(ck))
        return ans