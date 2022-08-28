"""
139. 单词拆分
https://leetcode.cn/problems/word-break/
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        m = max(len(w) for w in wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(1, m + 1):
                if i - j + 1 >= 0 and s[i - j + 1:i + 1] in words and dp[i - j + 1]:
                    dp[i + 1] = True
                    break

        return dp[-1]
