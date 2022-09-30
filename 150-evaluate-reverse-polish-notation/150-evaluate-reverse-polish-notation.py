from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque([])
        for token in tokens:
            if token in ["*","+","-","/"]:
                b = stack.pop()
                a = stack.pop()
                if token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(a/b))
                elif token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
            else:
                stack.append(int(token))
        print(stack)
        return stack.pop()