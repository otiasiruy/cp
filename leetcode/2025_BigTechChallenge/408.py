class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        mp = {}
        end = False
        num = ""
        id = -1
        i = 0
        total = 0
        n = len(word)
        ab = ""

        if abbr.isdigit() and int(abbr) > n:
            return False

        for c in abbr:
            if c.isalpha():
                if num and num[0] != "0":
                    mp[id] = int(num)
                    j = 0
                    while j < mp[id]:
                        ab = ab + "*"
                        j += 1

                    num = ""
                    id = mp[id] + i
                    total += 1
                elif len(num) > 0 and num[0] != "0" and len(num) > 1:
                    return False
                elif len(num) == 1 and num[0] == "0":
                    return False

                ab = ab + c
            if c.isdigit():
                num += c
                if len(num) > 0 and len(num) > n:
                    return False
                if id == -1:
                    id = i
            else:
                total += 1
            i += 1

        if num:
            mp[id] = int(num)
            if len(num) > 0 and num[0] == "0" and len(num) > 1:
                return False
            if len(num) > 0 and len(num) > n:
                return False
            j = 0
            while j < mp[id]:
                ab = ab + "*"
                j += 1

        total = len(ab)

        if total != n:
            return False

        j = 0
        while j < n:
            if ab[j] != word[j] and ab[j] != "*":
                ab[j]
                return False
            j += 1

        return True
