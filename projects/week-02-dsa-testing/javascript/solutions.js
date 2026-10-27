function sortArray(nums) {
    return [...nums].sort((a, b) => a - b);
}

function mergeSortedArray(nums1, nums2) {
    const result = [];
    let i = 0;
    let j = 0;

    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] <= nums2[j]) {
            result.push(nums1[i++]);
        } else {
            result.push(nums2[j++]);
        }
    }

    return result.concat(nums1.slice(i), nums2.slice(j));
}

function rotateArray(nums, k) {
    if (nums.length === 0) return [];

    k = ((k % nums.length) + nums.length) % nums.length;
    return k === 0
        ? [...nums]
        : nums.slice(-k).concat(nums.slice(0, -k));
}

function thirdMaximum(nums) {
    const distinct = [...new Set(nums)].sort((a, b) => b - a);
    return distinct.length >= 3 ? distinct[2] : distinct[0];
}

function checkSortedRotated(nums) {
    if (nums.length === 0) return true;

    let drops = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > nums[(i + 1) % nums.length]) {
            drops++;
        }
    }

    return drops <= 1;
}

module.exports = {
    sortArray,
    mergeSortedArray,
    rotateArray,
    thirdMaximum,
    checkSortedRotated
};