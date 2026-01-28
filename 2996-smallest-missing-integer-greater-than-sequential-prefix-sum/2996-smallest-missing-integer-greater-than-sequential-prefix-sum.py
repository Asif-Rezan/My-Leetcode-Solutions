class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = nums[0]
        for i in range(1, len(nums)): 
            if nums[i] == nums[i-1] + 1 :
                prefix_sum = prefix_sum + nums[i]

            else:
                break
        
        num_set = set(nums)
        x = prefix_sum

        while x in num_set: 
            x += 1

        return x