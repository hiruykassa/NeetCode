class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num not in seen.keys():
                seen[num] = 1
            else:
                seen[num] += 1
        
        return heapq.nlargest(k, seen, key=seen.get)

