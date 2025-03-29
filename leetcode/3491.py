from typing import List


class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        for number in numbers:
            c = 0
            for n in numbers:
                if n.startswith(number):
                    c += 1
                if c > 1:
                    return False
        return True