class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)-1
        water=0
        left,right= 0, n
        while left<right:
            cur_water=min(heights[left],heights[right])*(right-left)
            water= max(water,cur_water)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return water