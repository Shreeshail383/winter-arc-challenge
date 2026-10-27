const test = require('node:test');
const assert = require('node:assert/strict');

const {
    sortArray,
    mergeSortedArray,
    rotateArray,
    thirdMaximum,
    checkSortedRotated
} = require('./solutions');

// 1. Sort Array
test('sortArray handles edge cases', () => {
    assert.deepEqual(sortArray([]), []);
    assert.deepEqual(sortArray([5]), [5]);
    assert.deepEqual(sortArray([3, 1, 3, -2]), [-2, 1, 3, 3]);
});

// 2. Merge Sorted Arrays
test('mergeSortedArray handles edge cases', () => {
    assert.deepEqual(mergeSortedArray([], []), []);
    assert.deepEqual(mergeSortedArray([], [-2, 1]), [-2, 1]);
    assert.deepEqual(mergeSortedArray([1], [1]), [1, 1]);
    assert.deepEqual(
        mergeSortedArray([-3, 0], [-2, 4]),
        [-3, -2, 0, 4]
    );
});

// 3. Rotate Array
test('rotateArray handles edge cases', () => {
    assert.deepEqual(rotateArray([], 3), []);
    assert.deepEqual(rotateArray([7], 5), [7]);
    assert.deepEqual(rotateArray([1, 2, 3], 0), [1, 2, 3]);
    assert.deepEqual(rotateArray([1, 2, 3], 5), [2, 3, 1]);
    assert.deepEqual(rotateArray([-2, -1, 0], 1), [0, -2, -1]);
});

// 4. Third Maximum
test('thirdMaximum handles edge cases', () => {
    assert.equal(thirdMaximum([1]), 1);
    assert.equal(thirdMaximum([3, 2]), 3);
    assert.equal(thirdMaximum([3, 2, 1]), 1);
    assert.equal(thirdMaximum([2, 2, 3, 1]), 1);
    assert.equal(thirdMaximum([-1, -2, -3]), -3);
});

// 5. Check Sorted and Rotated
test('checkSortedRotated handles edge cases', () => {
    assert.equal(checkSortedRotated([]), true);
    assert.equal(checkSortedRotated([1]), true);
    assert.equal(checkSortedRotated([1, 1, 1]), true);
    assert.equal(checkSortedRotated([3, 4, 1, 2]), true);
    assert.equal(checkSortedRotated([2, 1, 3, 4]), false);
    assert.equal(checkSortedRotated([-3, -2, -4]), true);
});