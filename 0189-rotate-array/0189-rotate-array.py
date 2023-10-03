class Solution(object):
    def rotate(self, nums, k):

        k = k % len(nums)

        l,r = 0, len(nums) -1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l,r = 0, k -1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l,r = k , len(nums) -1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        

    #   res = [0] * len(nums)
      
    #   for i in range(len(nums)):
    #       if i < k:
    #         print(i)
    #         res[i+k] = nums[i]
    #       else:
    #           index = (i+k) % len(nums)
    #         #  res[index] = nums[i]
    #   return res
 

        