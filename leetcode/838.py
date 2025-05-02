class Solution:
    def pushDominoes(self, dn: str) -> str:
        r = 0
        n = len(dn)
        dom = list(dn)
        i = 0
        while i < n:
            if dom[i] == 'R':
                r = i + 1
                while r < n and dom[r] == '.':
                    r += 1
                if r < n and dom[r] == 'L':
                    l = r - 1
                    r = i + 1
                    while r < l:
                        dom[r] = 'R'
                        dom[l] = 'L'
                        l -= 1
                        r += 1
                else:
                    r = i + 1
                    while r < n and dom[r] == '.':
                        dom[r] = 'R'
                        r += 1
            elif dom[i] == 'L':
                l = i - 1
                while l >= 0 and dom[l] == '.':
                    l -= 1
                if dom[l] == 'R':
                    r = l + 1
                    l = i - 1
                    while r < l:
                        dom[r] = 'R'
                        dom[l] = 'L'
                        r += 1
                        l -= 1
                else:
                    l = i - 1
                    while l >= 0 and dom[l] == '.':
                        dom[l] = 'L'
                        l -= 1

            i += 1

        return ''.join(dom)