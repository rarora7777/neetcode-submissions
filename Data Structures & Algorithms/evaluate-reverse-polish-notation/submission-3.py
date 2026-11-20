class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            match token:
                case '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b + a)
                case '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                case '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)
                case '/':
                    a = stack.pop()
                    b = stack.pop()
                    x = b / a
                    x = int(math.floor(x)) if x >= 0 else int(math.ceil(x))
                    stack.append(x)
                case _:
                    stack.append(int(token))
        
        return stack[0]