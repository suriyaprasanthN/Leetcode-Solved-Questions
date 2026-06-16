class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        maxProxit =0
        minPurchase =prices[0]
        for i in range(1,len(prices)):
            maxProxit =max(maxProxit,prices[i] - minPurchase)
            minPurchase =min(minPurchase,prices[i])
        return maxProxit


