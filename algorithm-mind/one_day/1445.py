"""
1455. 检查单词是否为句中其他单词的前缀
https://leetcode.cn/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if not sentence:
            return -1
        word_list = sentence.split(" ")
        res = 0
        for w in word_list:
            if w.startswith(searchWord):
                return res + 1
            else:
                res += 1

        return -1
