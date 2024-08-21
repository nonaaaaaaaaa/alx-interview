#!/usr/bin/python3
"""Making Change Problem"""


def make_change(coins, total):
    """Determines the fewest number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] <= total else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    total = 11
    print(make_change(coins, total))  # Output: 3 (11 = 5 + 5 + 1)
