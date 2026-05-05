class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        map=defaultdict()
        heap=[]
        ret=[]
        for p in points:
            dist = math.sqrt((p[0] - 0)**2 + (p[1] - 0)**2)
           
            heapq.heappush(heap,(dist,p))
        
        for _ in range(k):
            dist, p=heapq.heappop(heap)
            ret.append(p)
        print(heap)
        return ret