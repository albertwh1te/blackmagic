from typing import List


def coins_change(coins: List[int], target: int) -> int:
    dp = [0 for _ in range(target + 1)]
    for i in range(target + 1):
        tmp = []
        for coin in coins:
            if (i - coin) >= 0:
                tmp.append(dp[i - coin] + 1)
        if tmp:
            dp[i] = min(tmp)
    print(dp)
    return dp[target]


if __name__ == "__main__":
    coins = [1, 2, 5]
    target = 11
    print(coins_change(coins, target))
