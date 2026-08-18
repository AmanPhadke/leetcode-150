class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        l = 0
        maxim = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            maxim = max(maxim, r - l + 1)

        return maxim
        
    #     seen = set()
    #     maxim = 0
    #     count = 0

    #     l, r = 0, 0

    #     while r < len(s):
    #         if s[r] not in seen:
    #             count += 1
    #             seen.add(s[r])
    #             maxim = max(maxim, count)
    #             r += 1

    #         else:
    #             count = 0
    #             seen = set()
    #             r = l + 1
    #             l += 1
                

    #     return maxim
        