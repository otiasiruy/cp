class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        i1 = i2 = 0
        ans = []
        for i in range(n1 + n2):
            if i1 < n1 and i2 < n2:
                if i % 2 == 0:
                    ans.append(word1[i1])
                    i1 += 1
                else:
                    ans.append(word2[i2])
                    i2 += 1
            else:
                if i1 < n1:
                    ans.append(word1[i1])
                    i1 += 1
                else:
                    ans.append(word2[i2])
                    i2 += 1

        return "".join(ans)