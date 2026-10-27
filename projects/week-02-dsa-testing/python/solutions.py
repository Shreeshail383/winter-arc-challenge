def sort_array(nums):
    return sorted(nums)


def merge_sorted_array(nums1, nums2):
    result = []
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    result.extend(nums1[i:])
    result.extend(nums2[j:])
    return result


def rotate_array(nums, k):
    if not nums:
        return []

    k %= len(nums)
    return nums[-k:] + nums[:-k] if k else nums[:]


def third_maximum(nums):
    distinct = sorted(set(nums), reverse=True)
    return distinct[2] if len(distinct) >= 3 else distinct[0]


def check_sorted_rotated(nums):
    if not nums:
        return True

    drops = sum(
        nums[i] > nums[(i + 1) % len(nums)]
        for i in range(len(nums))
    )
    return drops <= 1