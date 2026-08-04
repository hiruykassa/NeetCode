class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        l, r = 0, len(heights) - 1

        
        for l in range(len(heights)):
            while l < r:
                area = (min(heights[l], heights[r])) * (r - l)
                areas.append(area)
                r -= 1
            l += 1
            r = len(heights) - 1
        
        return max(areas)
