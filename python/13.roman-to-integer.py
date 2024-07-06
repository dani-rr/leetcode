#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_list = list(s)
        roman_dict = {
                        'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000,
                    }
        result = 0
        for i in range(len(roman_list) -1, -1, -1):
            if i == len(list(s)) - 1:
                result += roman_dict[roman_list[i]]
            elif roman_dict[roman_list[i]] < roman_dict[roman_list[i + 1]]:
                result -= roman_dict[roman_list[i]]
            else:
                result += roman_dict[roman_list[i]]
        return result

            # @lc code=end

