class Solution(object):
    def findTheDifference(self, s, t):
        
        sum_s, sum_t = 0,0

        for i in s:
            sum_s += ord(i)
        
        for j in t:
            sum_t += ord(j)

        return chr(sum_t - sum_s)

        


        