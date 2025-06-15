class Solution:
    def maxDiff(self, num: int) -> int:
        n = str(num)
        j = 0
        a = num
        while j < len(n):
            if n[j] != '9':
                a = n.replace(n[j], '9')
                break
            j += 1

        b = num
        i = 0
        mn = 0
        while i < len(n):
            if n[i] != '1' and n[i] != '0':
                if i > 0:
                    b = n.replace(n[i], '0')
                else:
                    b = n.replace(n[i], '1')
                break
            i += 1
        return int(a) - int(b)