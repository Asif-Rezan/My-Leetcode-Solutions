class Solution(object):
    def trap(self, height):

        if not height: return 0

        l,r = 0, len(height) -1
        leftMax,rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += max(0, leftMax - height[l])
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += max(0, rightMax - height[r])

        return res



        