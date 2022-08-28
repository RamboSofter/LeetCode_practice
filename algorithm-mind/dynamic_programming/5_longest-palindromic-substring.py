"""
5. 最长回文子串
https://leetcode.cn/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        dp[i][j] 表示s[i:j]是不是回文子串
        每次判断dp[i][j]更新max_len 和最长的起始索引start
        边界：当子串只有一个时，肯定是回文串，即 j-i + 1 < 2
        '''
        length = len(s)

        if length <= 1:
            return s

        dp = [[False] * length for _ in range(length)]  # 建立n x n 的矩阵，来判断是不是回文串

        for i in range(length):
            # 对角线上自己肯定是回文串
            dp[i][i] = True

        start = 0  # 用于记录最长串的开始索引
        max_len = 1

        for j in range(1, length):
            for i in range(j):
                # 头尾字符串相等
                if s[i] == s[j]:
                    # 且中间只有一个或0个
                    if (j - 1) - (i + 1) <= 0:
                        dp[i][j] = True
                    else:
                        # 否则和前一个状态相同
                        dp[i][j] = dp[i + 1][j - 1]
                # 如果是回文串
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i

        return s[start: start + max_len]
