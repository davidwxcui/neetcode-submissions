class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        neg_nums= [-x for x in nums]
        heapq.heapify(neg_nums)
        count=0
        for _ in range(k-1):
            heapq.heappop(neg_nums)
        return -heapq.heappop(neg_nums)
            

