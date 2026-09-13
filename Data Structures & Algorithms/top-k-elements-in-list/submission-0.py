class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        freqDict = sorted(freqDict.items(), key=lambda kv: kv[1] , reverse=True)
        ans = []
        
        for key, value in freqDict[:k]:
            ans.append(key)
        return ans

