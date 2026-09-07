class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        Output = []
        for i in range(n-1):
            for j in range(i+1,n):
                if i == j:
                    j+= 1
                if nums[i] + nums[j] == target:
                    Output = [i,j]
                    return Output
        
        
                



        