class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums) #automatically counts frequency
        buckets = [0] * (n+1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
            
        #Collect the output
        ret = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
        return ret

