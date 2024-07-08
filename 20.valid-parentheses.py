#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        result =  []
        for i in s:
            if i in '[({':
                result.append(i)
            else:
                if not result or \
                (i == ')' and result[-1] !='(') or \
                (i == ']' and result[-1] !='[') or \
                (i == '}' and result[-1] !='{'):
                    return False
                else:
                    result.pop()
        return not result
            

# @lc code=end
