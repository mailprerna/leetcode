class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # print(len(nums))
        newarray = [0]*len(nums)
        # print(newarray)
        for i in range(0,len(nums)):
            newarray[(i+k)%len(nums)] = nums[i]
        # print(newarray)
        nums.clear()
        nums = [nums.append(i) for i in newarray]
        
            
            
    
        
            
        
       class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(len(nums))
        newarray = [nums[(i+k)%len(nums)] for i in range(0,len(nums))]
        # print(newarray)
        nums.clear()
        nums = [nums.append(i) for i in newarray]
