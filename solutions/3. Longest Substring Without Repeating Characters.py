class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        left = -1
        res = 0        
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] > left:
                left = dic[s[i]]
            dic[s[i]] = i
            res = max(res, i-left)
        return res
​
