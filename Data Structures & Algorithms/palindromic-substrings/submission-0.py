class Solution:
    def countSubstrings(self, s: str) -> int:
        dp: list[list[bool]] = [[False for _ in range(len(s))] for _ in range(len(s))]
        count: int = 0
        for left in range(len(s)-1, -1, -1):
            for right in range(left, len(s)):
                if left == right:
                    dp[left][right] = True
                elif right == left + 1:
                    dp[left][right] = (s[left] == s[right])
                else:
                    dp[left][right] = ((s[left] == s[right]) and dp[left+1][right-1])
                count += int(dp[left][right])
        return count