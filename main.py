def kbig(nums, k):
    maximal = 0
    if k > len(nums):
        return nums
    for i in range(k):
        maximal = max(nums)
        nums.remove(max(nums))
    return maximal
