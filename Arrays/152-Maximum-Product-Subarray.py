'''Leetcode - https://leetcode.com/problems/maximum-product-subarray/'''

'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Input: nums = [2,3,-2,4]
Output: 6
'''

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
