from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - (stack[-1] + 1)
                max_area = max(max_area, height * width)

            stack.append(i)
        
        return max_area