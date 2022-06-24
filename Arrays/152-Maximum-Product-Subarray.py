'''Leetcode - https://leetcode.com/problems/maximum-product-subarray/'''

# Solution1
def maxProduct(nums):
    if(len(nums)) == 0:
        return 0
    maxp = nums[0]
    for i in range(len(nums)):
        currp = 1
        for j in range(i, len(nums)):
            currp *= nums[j]
            maxp = max(maxp, currp)
    return maxp

# T:O(N^2)
# S:O(1)

# Solution2
def maxProduct(nums):
    if(len(nums)) == 0:
        return 0
    curr_max = nums[0]
    curr_min = nums[0]
    result = curr_max

    for i in range(len(nums)):
        curr = nums[i]
        temp_max = max(curr, curr_max*curr_min*curr)
        curr_min = min(curr, curr_max*curr_min*curr)
        curr_max = temp_max
        result = max(curr_max, result)
    return result

# T:O(N)
# S:O(1)
