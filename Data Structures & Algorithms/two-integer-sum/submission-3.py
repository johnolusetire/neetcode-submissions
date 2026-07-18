class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i, num in enumerate(nums):
            if num in track:
                return [track[num], i]
            track[target - num] = i
        
        return [0,0]