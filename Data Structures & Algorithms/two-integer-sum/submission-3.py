class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        hashmap = {}
        j = 0 
        for i in nums:
            hashmap[i] = j
            j = j + 1
        k = 0
        for i in nums:
            diff = target - i
            if diff in hashmap and k != hashmap[diff]:
                ans = [k, hashmap[diff]]
                return ans
            k = k+1