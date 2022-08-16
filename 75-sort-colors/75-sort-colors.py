class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        RED, WHITE, BLUE = 0, 1, 2
        
        # two pointers for RED as well as BLUE
        idx_red, idx_blue = 0, len(nums)-1
        
        i = 0
        while i <= idx_blue :
            
            if nums[i] == RED:
                
                nums[idx_red], nums[i] = nums[i], nums[idx_red]
                
                # update idx for red
                idx_red += 1
            
            
            elif nums[i] == BLUE:
            
                nums[idx_blue], nums[i] = nums[i], nums[idx_blue]
                
                # update idx for blue
                idx_blue -= 1
                
                # i-1 in order to stay and do one more color check on next iteration
                i -= 1
            
            
            # i move forward
            i += 1                