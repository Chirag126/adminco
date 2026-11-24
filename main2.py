def two_sum(nums, target):
    pairs = sorted((n, i) for i, n in enumerate(nums))
    left, right = 0, len(pairs) - 1
    while left < right:
        total = pairs[left][0] + pairs[right][0]
        if total == target:
            return sorted([pairs[left][1], pairs[right][1]])
        if total < target: left += 1
        else: right -= 1
print(two_sum([3, 2, 4], 6))