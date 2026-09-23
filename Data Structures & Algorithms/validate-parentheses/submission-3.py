class Solution:

    def isSameType(self, a: str, b:str) -> bool:
        if (a=="(" and b==")") or (a=="{" and b=="}") or (a=="[" and b=="]"):
            return True
        return False
        
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c=="(" or c=="{" or c=="[":
                stack.append(c)
            else:
                if len(stack)!=0 and self.isSameType(stack[-1], c):
                    stack.pop()
                else:
                    return False

        if len(stack)==0:
            return True
        else:
            return False
