from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        # Step 1: Check if a palindrome can be formed
        odd_chars = [char for char, freq in cnt.items() if freq % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Step 2: Prepare the character pool for the first half
        half_cnt = {char: freq // 2 for char, freq in cnt.items() if freq // 2 > 0}
        unique_chars = sorted(half_cnt.keys())
        
        m = n // 2  # Length of the first half
        res_half = []
        
        def dfs(idx, is_greater):
            if idx == m:
                # Construct the full palindrome: first_half + mid_char + reversed(first_half)
                first_str = "".join(res_half)
                full_str = first_str + mid_char + first_str[::-1]
                return full_str if full_str > target else ""
            
            # Try each available character in ascending order for lexicographical smallest
            for char in unique_chars:
                if half_cnt[char] > 0:
                    target_char = target[idx]
                    
                    # Pruning: if we are not yet strictly greater, we cannot pick a character smaller than target[idx]
                    if not is_greater and char < target_char:
                        continue
                    
                    # Choose
                    half_cnt[char] -= 1
                    res_half.append(char)
                    
                    next_is_greater = is_greater or (char > target_char)
                    
                    # Explore
                    sub_result = dfs(idx + 1, next_is_greater)
                    if sub_result:
                        return sub_result
                    
                    # Backtrack
                    res_half.pop()
                    half_cnt[char] += 1
            
            return ""

        return dfs(0, False)