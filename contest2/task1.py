from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
    
        stack = []  
        water = 0  
        
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                cur_bottom = stack.pop()

                if not stack:
                    break

                left = stack[-1]
                width = i - left - 1
                diff_height = min(height[i], height[left]) - height[cur_bottom]
                water += width * diff_height

            stack.append(i)

        return water