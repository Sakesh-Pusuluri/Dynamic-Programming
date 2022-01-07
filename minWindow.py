class Solution:
    def minWindow(self, str1: str, pattern: str) -> str:
        window_start, matched, substr_start = 0, 0, 0
        min_length = len(str1) + 1
        char_frequency = {}
        for chr in pattern:
            char_frequency[chr]=char_frequency.get(chr,0)+1
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char in char_frequency:
                char_frequency[right_char] -= 1
                if char_frequency[right_char] >= 0: 
                    matched += 1
            while matched == len(pattern):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    substr_start = window_start
                left_char = str1[window_start]
                window_start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1
        if min_length > len(str1):
            return ""
        return str1[substr_start:substr_start + min_length]
      
      
# Time complexity - O(n)
# Space complexity - O(1)
