class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash_table = {}

        n = len(nums)

        for i in range(n):
            if nums[i] not in hash_table:
                hash_table[nums[i]] = True
            else:
                return True 
        return False
        