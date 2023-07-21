# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Create a function that returns the maximum profit you can achieve from 
# this transaction. If you cannot achieve any profit, return 0.
# You are given an array prices where prices[i] is the price of a given 
# stock on the ith day. You want to maximize your profit by choosing a single 
# day to buy one stock and choosing a different day in the future to sell that stock.

# Input: prices = [7,1,5,3,6,4] -> 5
# Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

def buy_sell(price_list):

    max_profit = 0

    for i in range(len(price_list)):
        for j in range(i+1, len(price_list)):
            if price_list[j] - price_list[i] > max_profit:
                max_profit = price_list[j] - price_list[i]

    return max(0, max_profit)

prices = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

print(buy_sell(prices2))



def buy_sell2(price_list):
    left = 0 #buy
    right = 1 #sell
    max_profit = 0

    while right < len(price_list):
        if price_list[left] < price_list[right]: # checks if profitable
            profit = price_list[right] - price_list[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1
    
    return max_profit

print(f"This is solution 2: {buy_sell2(prices)}")



def buy_sell3(price_list):
    left = 0  # buy
    max_profit = 0

    for right in range(1, len(price_list)):
        if price_list[right] - price_list[left] > max_profit:
            max_profit = price_list[right] - price_list[left]
        elif price_list[right] < price_list[left]:
            left = right

    return max_profit


print(f"This is solution 3: {buy_sell3(prices)}")



def buy_sell4(price_list):
    left = 0  # buy
    right = 1  # sell
    max_profit = 0

    while right < len(price_list):
        if price_list[right] - price_list[left] > max_profit:
            max_profit = price_list[right] - price_list[left]
        elif price_list[right] < price_list[left]:
            left = right
        right += 1

    return max_profit

print(f"This is solution 4: {buy_sell4(prices)}")