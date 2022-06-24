'''Leetcode - https://leetcode.com/problems/two-sum/ '''

# Solution1
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
# T:O(N^2)
# S:O(1)

# Solution2 hashmap


def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in dict:
            return [dict[diff], i]
        dict[nums[i]] = i

# T: O(N)
# S: O(N)
