class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p=0
        max_buy=prices[0]
        for p in prices:
            max_p= max(max_p, p-max_buy)
            max_buy= min(p, max_buy)
        return max_p

