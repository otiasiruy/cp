class Solution:
    def maxSubstringLength(self, s: str) -> int:

        loc = defaultdict(list)
        for i, ch in enumerate(s):
            loc[ch].append(i)

        def check(l, r):
            for ch in loc:
                lc = bisect.bisect_left(loc[ch], l)
                rc = bisect.bisect_right(loc[ch], r)
                count_in_range = rc - lc

                if not (count_in_range == 0 or count_in_range == len(loc[ch])):
                    return False
            return True

        n = len(s)
        ans = -1
        for ch1 in loc:
            li = loc[ch1][0]
            for ch2 in loc:
                ri = loc[ch2][-1]
                if li > ri or ri - li + 1 == n:
                    continue
                if check(li, ri):
                    ans = max(ans, ri - li + 1)
        return ans
