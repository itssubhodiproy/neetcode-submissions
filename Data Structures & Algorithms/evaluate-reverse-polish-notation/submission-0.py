class Solution:
    def operation(self, a: int, b: int, op: str) -> int:
        ans = 0
        if op=="+":
            ans = a+b
        elif op =="-":
            ans = a-b
        elif op =="*":
            ans = a*b
        else:
            ans = int(a/b)
        return ans

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in ('+', '-', '*', '/'):
                b = stack.pop()
                a = stack.pop()
                stack.append(self.operation(a, b, tok))
            else:
                stack.append(int(tok))
        return stack[-1]