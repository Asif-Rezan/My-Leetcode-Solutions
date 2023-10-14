class Solution(object):
    def searchMatrix(self, matrix, target):
        
        res_row = []
        for i in matrix:

            
            print(i[0])
            print(i[-1])

            if target >= i[0] and target <= i[-1]:
                res_row = i
             
    
            
        l,r = 0, len(res_row)-1

        print(res_row)

        while l <= r:
            mid = l + ((r-l) // 2)
            print(mid)


            if res_row[mid] > target:
                r = mid - 1
                print(mid)
            elif res_row[mid] < target:
                l = mid + 1
                print(mid)
            else:
                return True
        
        return False
        
           