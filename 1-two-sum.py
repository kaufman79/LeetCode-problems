
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}

        # Find the complement
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [i, num_map[complement]]
            num_map[nums[i]] = i  # build hash map as we go. Key is int, value is index in nums

        return []  # no complement


solution = Solution()
print(solution.twoSum([3, 2, 4], target=6))
