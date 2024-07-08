def isValid(s) -> bool:
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
            
isValid("([)]")