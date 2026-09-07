class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for index, num in enumerate(nums):
            A.append([num, index])

        A.sort()

        i = 0
        j = len(A) - 1

        while i < j:
            ans = A[i][0] + A[j][0]

            if ans == target:
                return sorted([A[i][1], A[j][1]])
            elif ans < target:
                i += 1
            else:
                j -= 1

        return []