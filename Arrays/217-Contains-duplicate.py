'''Leetcode - https://leetcode.com/problems/contains-duplicate/'''

# Solution1
def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
            return False

# T:O(N^2)
# S:O(1)


# Solution2
def containsDuplicate(nums):
    hashset = set()

    for i in len(nums):
        if nums[i] in hashset:
            return True
        hashset.add(nums[i])
    return False

# T: O(N)
# S: O(N)

# Solution3
def containsDuplicate(nums):
    nums.sort()

    for i in len(1, nums):
        if nums[i] == nums[i-1]:
            return True
        return False

# T: O(nlogN)
# S: O(1)
