from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        ans = []
        for i in range(len(currentState) - 1):
            if currentState[i] + currentState[i + 1] == "++":
                p1 = ''
                if i > 0:
                    p1 = currentState[: i]
                p2 = ''
                if i < len(currentState) - 1:
                    p2 = currentState[i + 2:]
                ans.append(p1 + "--" + p2)
        return ans