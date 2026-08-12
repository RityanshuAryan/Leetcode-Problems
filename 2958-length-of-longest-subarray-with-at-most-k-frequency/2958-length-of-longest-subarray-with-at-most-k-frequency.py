from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Dictionary to track frequency of each element in current window
        frequency_map = defaultdict(int)
      
        # Initialize result and left pointer of sliding window
        max_length = 0
        left = 0
      
        # Iterate through array with right pointer
        for right, current_num in enumerate(nums):
            # Add current element to window by incrementing its frequency
            frequency_map[current_num] += 1
          
            # Shrink window from left while current element's frequency exceeds k
            while frequency_map[current_num] > k:
                # Remove leftmost element from window
                frequency_map[nums[left]] -= 1
                # Move left pointer forward
                left += 1
          
            # Update maximum length found so far
            # Window size is (right - left + 1)
            max_length = max(max_length, right - left + 1)
      
        return max_length
