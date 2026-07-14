class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        cons = set()

        left, right = 0, len(nums) - 1

        while left != len(nums) and right != -1 and left != right:
            if nums[left] == nums[right] + 1 or nums[right] == nums[left] + 1:
                cons.add(nums[left])
                cons.add(nums[right])
                
            right -= 1
            if right == left + 1:
                left += 1
                right = len(nums) - 1

        return len(cons)
                    