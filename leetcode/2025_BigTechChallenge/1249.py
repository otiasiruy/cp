class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = set()
        r = set()
        ans = []
        for i in range(len(s)):
            if s[i] == '(':
                l.add(i)
            elif s[i] == ')' and len(l) > len(r):
                r.add(i)
        nr = len(r)
        nl = nr
        for i in range(len(s)):
            if i in l and nl > 0:
                ans.append(s[i])
                l.remove(i)
                nl -= 1
            elif i in r:
                ans.append(s[i])
                r.remove(i)
                nr -= 1
            elif s[i] != '(' and s[i] != ')':
                ans.append(s[i])
        return ''.join(ans)