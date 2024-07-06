def longestCommonPrefix(strs) -> str:
    shortest = len(min(strs, key=len))
    result = ''
    if len(strs) == 1:
        return strs[0]  
    for n in range(0, shortest):
        for i in range(0, len(strs) - 1):
            if strs[i][n] == strs[i + 1][n]:
                if i == len(strs) - 2:
                    result += strs[i][n]
                continue
            else:
                return result
    return result

longestCommonPrefix(["",""])