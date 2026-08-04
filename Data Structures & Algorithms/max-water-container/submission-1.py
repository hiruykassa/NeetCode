class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1

        for l in range(len(heights)):
            while l < r:
                new_area = (r-l) * min(heights[l], heights[r])
                area = max(new_area, area)
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r-= 1
        
        return area
