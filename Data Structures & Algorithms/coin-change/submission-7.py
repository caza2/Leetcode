import sys
sys.setrecursionlimit(20_000)

class Solution:
    # Top-down
    def coinChange(self, coins: List[int], amount: int) -> int:
        m: int = min(coins)
        dp: dict[int, int] = {0: 0}
        def f(target: int) -> int:
            if target in dp:
                return dp[target]
            if target < m:
                dp[target] = -1
            else:
                _temp: list[int] = []
                for coin in coins:
                    if coin <= target:
                        dp[target - coin] = f(target - coin)
                        if dp[target - coin] != -1 :
                            _temp.append(dp[target - coin])
                if not _temp:
                    dp[target] = -1    
                else:
                    dp[target] = 1 + min(_temp)
            return dp[target]
        return f(amount)