import pytest

from solutions import (
    sort_array,
    merge_sorted_array,
    rotate_array,
    third_maximum,
    check_sorted_rotated,
)


# 1. Sort Array
@pytest.mark.parametrize("nums, expected", [
    ([], []),
    ([5], [5]),
    ([3, 1, 3, -2], [-2, 1, 3, 3]),
    ([-5, -1, -3], [-5, -3, -1]),
])
def test_sort_array(nums, expected):
    assert sort_array(nums) == expected


# 2. Merge Sorted Arrays
@pytest.mark.parametrize("a, b, expected", [
    ([], [], []),
    ([], [-2, 1], [-2, 1]),
    ([1], [1], [1, 1]),
    ([-3, 0], [-2, 4], [-3, -2, 0, 4]),
])
def test_merge_sorted_array(a, b, expected):
    assert merge_sorted_array(a, b) == expected


# 3. Rotate Array Right
@pytest.mark.parametrize("nums, k, expected", [
    ([], 3, []),
    ([7], 5, [7]),
    ([1, 2, 3], 0, [1, 2, 3]),
    ([1, 2, 3], 5, [2, 3, 1]),
    ([-2, -1, 0], 1, [0, -2, -1]),
])
def test_rotate_array(nums, k, expected):
    assert rotate_array(nums, k) == expected


# 4. Third Maximum
@pytest.mark.parametrize("nums, expected", [
    ([1], 1),
    ([3, 2], 3),
    ([3, 2, 1], 1),
    ([2, 2, 3, 1], 1),
    ([-1, -2, -3], -3),
])
def test_third_maximum(nums, expected):
    assert third_maximum(nums) == expected


# 5. Check Sorted and Rotated
@pytest.mark.parametrize("nums, expected", [
    ([], True),
    ([1], True),
    ([1, 1, 1], True),
    ([3, 4, 1, 2], True),
    ([2, 1, 3, 4], False),
    ([-3, -2, -4], True),
])
def test_check_sorted_rotated(nums, expected):
    assert check_sorted_rotated(nums) == expected