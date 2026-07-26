class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for i,val in enumerate(nums):
            diff = target-val
            if diff in output:
                return [output[diff],i]
            output[val] = i