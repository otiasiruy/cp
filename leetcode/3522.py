from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        score = 0
        i = 0
        seen = set()
        while 0 <= i < n and i not in seen:
            seen.add(i)
            if instructions[i] == "add":
                score += values[i]
                i += 1
            else:
                i += values[i]
        return score