class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_array = [x**2 for x in nums]
        return sorted(square_array)
      
      
