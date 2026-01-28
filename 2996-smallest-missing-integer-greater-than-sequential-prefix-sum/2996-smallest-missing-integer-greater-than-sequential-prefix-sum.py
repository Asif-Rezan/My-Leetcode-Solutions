class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        prefix_sum = nums[0]
        for i in range(1, len(nums)): 
            if nums[i] == nums[i-1] + 1 :
                prefix_sum = prefix_sum + nums[i]

            else:
                break


        nums.sort()

        for i in range(n):
            if prefix_sum == nums[i]:
                prefix_sum += 1
        return prefix_sum