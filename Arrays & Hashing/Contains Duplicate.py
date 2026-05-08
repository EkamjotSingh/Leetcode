class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return True
            duplicate.add(num)
        else:
            return False


nums = [1,2,3,4,4]
print(Solution().hasDuplicate(nums))