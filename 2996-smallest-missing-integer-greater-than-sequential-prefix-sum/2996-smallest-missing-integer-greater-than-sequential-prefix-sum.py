from typing import List
from itertools import count

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Calculate sum of longest consecutive sequence starting from index 0
        consecutive_sum = nums[0]
        index = 1
      
        # Keep adding consecutive integers (each element is exactly 1 more than previous)
        while index < len(nums) and nums[index] == nums[index - 1] + 1:
            consecutive_sum += nums[index]
            index += 1
      
        # Create a set of all numbers in the array for O(1) lookup
        seen_numbers = set(nums)
      
        # Find the smallest integer >= consecutive_sum that is not in the array
        for candidate in count(consecutive_sum):
            if candidate not in seen_numbers:
                return candidate
