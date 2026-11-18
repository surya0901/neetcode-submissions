class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        
        hashset = set()
        for i in range (len(nums)):
            if nums[i] not in hashset:
                hashset.add(nums[i])
            else:
                return True
        return False 