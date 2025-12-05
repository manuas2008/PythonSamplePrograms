def max_profit(prices: list) -> int:
    max_prof = 0
    n = len(prices)
    for sell_idx in range(n-1, 0, -1):
        buy_idx = 0
        while buy_idx < sell_idx:
            max_prof = max(max_prof, prices[sell_idx] - prices[buy_idx])
            buy_idx += 1
    return(max_prof)


print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))
print(max_profit([1,2,3,4,5,6,7]))
