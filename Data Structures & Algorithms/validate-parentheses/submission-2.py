from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = deque()
        
        for ch in s:
            if ch in ['(', '{', '[']:
                brackets.append(ch)
            elif ch == ')':
                if len(brackets) == 0 or brackets[-1] != '(':
                    return False
                else:
                    brackets.pop()
            elif ch == ']':
                if len(brackets) == 0 or brackets[-1] != '[':
                    return False
                else:
                    brackets.pop()
            elif ch == '}':
                if len(brackets) == 0 or brackets[-1] != '{':
                    return False
                else:
                    brackets.pop()
        
        return len(brackets) == 0        
        