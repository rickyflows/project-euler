#!/usr/bin/env python3
def next_permutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    if i == -1:
        return nums[::-1]
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    nums[i+1:] = reversed(nums[i+1:])
    return nums

nums = [i for i in range(10)]
for i in range(10**6 - 1):
    nums = next_permutation(nums)
print("".join(map(str, nums)))
