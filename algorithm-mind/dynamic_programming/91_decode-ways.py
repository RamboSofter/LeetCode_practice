"""
91. 解码方法
https://leetcode.cn/problems/decode-ways/
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        算法思路：动态规划
        '''
        # 如果以0开始说明无法解码，直接返回0
        if s.startswith('0'):
            return 0

        n = len(s)
        # dp[i] 表示前i个字符能反向映射的字母数量
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            # 看前两个字符如果不合规，直接返回0,无法解码
            if s[i - 1] == '0' and s[i - 2] not in '12':
                return 0
            # 10和20只能转换成一种
            if s[i-2: i] in ['10', '20']:
                dp[i] = dp[i - 2]
            # 11-26都有两种解法，一种合并，一种拆开
            elif '10' <= s[i-2: i] <= '26':
                dp[i] = dp[i - 1] + dp[i - 2]
            # 1-9只能是一种和前一个状态相同
            else:
                dp[i] = dp[i - 1]

        return dp[n]
