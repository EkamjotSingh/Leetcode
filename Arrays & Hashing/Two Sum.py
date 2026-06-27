class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[j] = i
        return

nums = [3,4,5,6]
target = 9

print(Solution().twoSum(nums, target))