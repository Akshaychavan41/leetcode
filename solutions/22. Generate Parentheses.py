class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backTrack(S = '', left = 0, right = 0):
            if len(S) == 2*n:
                ans.append(S)
                return
            if left < n:
                backTrack(S + '(' , left +1, right)
            if right< left:
                backTrack(S+')', left, right+1)
        backTrack() 
        return ans
