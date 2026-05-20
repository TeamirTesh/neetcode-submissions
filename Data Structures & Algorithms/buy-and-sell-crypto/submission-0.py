class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r, n = 0, 1, len(prices)
        
        while r < n:
            if prices[r] <= prices[l]:
                l = r
                r += 1
            else:
                profit = max(profit, prices[r] - prices[l])
                r += 1
        
        return profit

            

        