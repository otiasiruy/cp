from collections import Counter


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        j = 0
        for i in range(n):
            if target[i] == 'L':
                while j < n:
                    if start[j] == 'L' and j >= i:
                        j += 1
                        break
                    elif start[j] == 'L' and j < i:
                        return False
                    elif start[j] == 'R':
                        return False
                    j += 1
            elif target[i] == 'R':
                while j < n:
                    if start[j] == 'R' and j <= i:
                        j += 1
                        break
                    elif start[j] == 'R' and j > i:
                        return False
                    elif start[j] == 'L':
                        return False
                    j += 1
        sc = Counter(start)
        tc = Counter(target)
        if len(sc) != len(tc) or sc['L'] != tc['L'] or sc['R'] != tc['R']:
            return False
        return True