def centered_average(nums):
    nums_sorted = sorted(nums)
    return sum(nums_sorted[1:-1]) // (len(nums) - 2)
