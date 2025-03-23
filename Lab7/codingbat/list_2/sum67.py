def sum67(nums):
    total = 0
    in_skip = False
    for n in nums:
        if in_skip:
            if n == 7:
                in_skip = False
            continue
        if n == 6:
            in_skip = True
            continue
        total += n
    return total
