from PythonSamplePrograms import buy_sell_stock
import pytest


@pytest.mark.parametrize(
    "prices, expected",
    [
        # mixed increases and decreases -> buy at 1 sell at 6
        ([7, 1, 5, 3, 6, 4], 5),
        # strictly decreasing -> no profit possible
        ([7, 6, 4, 3, 1], 0),
        # strictly increasing -> profit is last - first
        ([1, 2, 3, 4, 5, 6, 7], 6),
        # single price -> cannot trade
        ([5], 0),
        # two prices decreasing -> no profit
        ([2, 1], 0),
        # two prices increasing -> small profit
        ([1, 2], 1),
        # constant prices -> zero profit
        ([3, 3, 3], 0),
        # zero price then higher -> large profit
        ([0, 4, 2, 8], 8),
    ],
    ids=[
        "mixed_increase_decrease",
        "monotonic_decrease_no_profit",
        "monotonic_increase_full_profit",
        "single_price_no_trade",
        "two_prices_decrease",
        "two_prices_increase",
        "constant_prices_no_profit",
        "zero_start_high_gain",
    ],
)
def test_max_profit(prices, expected):
    assert buy_sell_stock.max_profit(prices) == expected
