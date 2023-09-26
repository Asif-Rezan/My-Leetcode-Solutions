class Solution(object):
    def twoSum(self, numbers, target):

        left = 0
        right = len(numbers) - 1

      
        while left < right:
            sum = numbers[left] + numbers[right]

            if(sum > target):
                right = right -1
            
            elif(sum < target):
                left = left + 1
            
            else:
                return(left+1, right+1)







        # Time Limit Exceeded

        # sum = 0
        # output = []

        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):

        #         sum = sum + numbers[i] + numbers[j]


        #         if sum == target:
        #             output = [i+1, j+1]
        #             break
                
        #         sum = 0



                
        
        # return output

