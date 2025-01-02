class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [h for _, h in envelopes]
        from bisect import bisect_left
        dp = []
        for h in heights:
            idx = bisect_left(dp, h)
            dp.append(h) if idx == len(dp) else dp.__setitem__(idx, h)
        return len(dp)
