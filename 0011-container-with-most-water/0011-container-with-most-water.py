class Solution(object):
    def maxArea(self, height):
       
       l,r = 0, len(height) - 1
       area = 0
       result = 0


       while l < r:
           area = (r - l) * min(height[l], height[r])
           result = max(area, result)
           
           if height[l]< height[r]:
               l += 1
           else:
               r -= 1
        
       return result  



        