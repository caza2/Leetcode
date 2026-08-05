class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp: dict[tuple[int, int], bool] = {}
        def f(left: int, right: int) -> None:
            if right == left:
                dp[(left, right)] = True
            elif right == left + 1:
                dp[(left, right)] = (s[left] == s[right])
            else:
                if (left+1, right-1) not in dp:
                    f(left+1, right-1)
                dp[(left, right)] = (s[left] == s[right] and dp[(left+1, right-1)])

        for left in range(len(s)):
            for right in range(left, len(s)):
                f(left, right)
        max_length, max_pal = 1, s[0]
        for key in dp.keys():
            if dp[key] and key[1] - key[0] + 1 > max_length:
                max_length = key[1] - key[0] + 1
                max_pal = s[key[0]: key[1]+1]
        return max_pal