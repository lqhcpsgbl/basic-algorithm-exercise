class Solution:
    def isValid(self, s: str) -> bool:
        astack = []
        for c in s:
            if c in '({[':
              astack.append(c)
            elif c in ')}]':
              if not astack:
                return False
              else:
                poped = astack.pop()
                if c == ')' and poped != '(':
                    return False
                elif c == '}' and poped != '{':
                    return False
                elif c == ']' and poped != '[':
                    return False
        return True if not astack else False
