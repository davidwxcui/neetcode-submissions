class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m= defaultdict(int)
        heap= []
        ret=[]
        for n in nums:
            m[n]+=1
        for n in m:
            heapq.heappush(heap, (m[n],n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret