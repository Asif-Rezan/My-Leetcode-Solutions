class Solution(object):
    def isValid(self, s):
       
       stack = []
       openList = {")" : "(", "}" : "{", "]" : "["}
       for i in s:
           if i in openList:
               if stack and stack[-1] == openList[i]:
                   stack.pop()
               else:
                    return False
            
           else: stack.append(i)
        
       return True if not stack else False
            
        