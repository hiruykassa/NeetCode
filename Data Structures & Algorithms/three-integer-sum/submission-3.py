class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trip = set()
        new_num = sorted(nums)
        for i in range(len(new_num)):
                    l, r = i+1, len(new_num) - 1
                    while l < r:
                        if new_num[i] + new_num[l] + new_num[r] == 0:
                            trip.add(tuple((new_num[i], new_num[l], new_num[r])))
                        
                        l += 1
                        r -= 1
                    
        return list(trip)
