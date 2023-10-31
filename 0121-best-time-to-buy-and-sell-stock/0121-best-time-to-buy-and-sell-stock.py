class Solution(object):
    def maxProfit(self, prices):


        l,r = 0,1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)

            else:
                l = r
            
            r = r+1

        return maxProfit






        # min_price = min(prices)
        # max_price = max(prices)
        # temp_list= []
       

        

        # min_index = 0
        # max_index = 0
      

        # for i in range(len(prices)):
                
        #     if prices[i] == min_price:
        #         min_index = i
        #         break

        # for j in range(min_index,len(prices)):

        #     temp_list.append(prices[j])
             
             
            
        #      #print(prices[j])


        # # print(min_price)
        # max_price = max(temp_list)
        # print(max_price)
       

        # if min_price > max_price:
        #     return 0
        
        # else:
        #     return max_price - min_price
               



        
        
            


        """
        :type prices: List[int]
        :rtype: int
        """