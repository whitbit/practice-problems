def maxProfit(prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

def max_profit(prices):
        profit = 0    

        if len(prices) < 2:
            return profit
        
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                profit += prices[i+1] - prices[i]
        return profit
print max_profit([2, 3, 10, 1, 15])