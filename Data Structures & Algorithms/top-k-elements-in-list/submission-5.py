class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Build a Has Map (Dictionary) that sores numbers --> how many times it appeared
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0) #rememebr the this syntax
        #Buld the Min-Heap of size k
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num)) # Pushes a pair in to heap
            if len(heap) > k: # Removes the smallest element if heap is greater than k
                heapq.heappop(heap)
        
        #Extract the Answers
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res