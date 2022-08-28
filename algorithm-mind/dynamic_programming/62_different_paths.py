"""
62. 不同路径
https://leetcode.cn/problems/unique-paths/
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        memo = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i][j - 1] + memo[i - 1][j]

        return memo[m-1][n-1]
