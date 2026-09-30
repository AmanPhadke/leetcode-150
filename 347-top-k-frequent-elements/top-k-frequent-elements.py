class Solution(object):
    def topKFrequent(self, nums, k):
        freqHash = {}
        temp = []
        
        for num in nums:
            if num not in freqHash:
                freqHash[num] = 1

            else:
                freqHash[num] += 1
                

        for key, val in sorted(freqHash.items(),key = lambda x: x[1], reverse=True):
            if k !=0:
                temp.append(key)
            else:
                break
            k -= 1

        return sorted(temp)
            