class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        count=0
        for n in seen:
            if (n-1) not in seen:
                scount=1
                while (n+scount) in seen:
                    scount+=1
                count=max(count,scount)
        return count
                
            
