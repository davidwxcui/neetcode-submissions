class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m= defaultdict(int)
        for i, n in enumerate(nums):
            diff=target-n
            if n in m:
                return [m[n], i]
            else:
                m[diff]=i
        return []

            