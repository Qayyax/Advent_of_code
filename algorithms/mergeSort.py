def merge_sort(nums):
    n = len(nums)
    if n < 2:
        return nums
    median = n // 2
    left = nums[:median]
    right = nums[median:]
    sorted_left_side = merge_sort(left)
    sorted_right_side = merge_sort(right)
    return merge(sorted_left_side, sorted_right_side)


def merge(first, second):
    final = []
    while first and second:
        if first[0] > second[0]:
            final.append(second[0])
            second.pop(0)
        else:
            final.append(first[0])
            first.pop(0)
    while first:
        final.append(first[0])
        first.pop(0)
    while second:
        final.append(second[0])
        second.pop(0)

    return final
