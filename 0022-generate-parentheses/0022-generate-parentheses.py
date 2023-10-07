class Solution(object):
    def generateParenthesis(self, n):

        stack = []
        result = []

        def genarate(openN, closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                genarate(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                genarate(openN, closeN + 1)
                stack.pop()
        
        
        genarate(0,0)
        return result
        