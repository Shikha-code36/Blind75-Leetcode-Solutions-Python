'''Leetcode - https://leetcode.com/problems/contains-duplicate/'''

# Solution1
def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
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
