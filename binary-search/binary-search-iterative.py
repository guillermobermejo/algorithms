"""
Binary Search Algorithm Implementation (Iterative Version)

Programmer: Guillermo Bermejo

This implementation performs binary search on a sorted list to find the index of a target
value in an iterative manner. It repeatedly divides the search interval in half, leveraging
the sorted property of the input array to achieve logarithmic time performance.

Variants supported:
- Iterative approach
- Recursive approach

Requirements:
- The input list must be sorted in non-decreasing order

Applications:
- Efficient search in large sorted datasets
- Searching in databases, dictionaries, logs, etc.
- As a subroutine in advanced algorithms (e.g., search over answers, optimization)

Time Complexity: O(log n)
Space Complexity:
- Iterative: O(1)
- Recursive: O(log n) due to recursion stack

Pseudo Code (Iterative Version):
    declare & initialize:
        1 int value     name: l     value: 0                notes: left pointer
        1 int value     name: r     value: len(nums)-1      notes: right pointer

    while loop (l <= r):
        declare and initialize:
            1 int value     name: m     value: int((l+r)/2) notes: middle value (the return)

        if check:
            if nums[m] == target
                true ? we FOUND target, return m
                false ? continue this iteration of the loop (calculate pointers)

        calculate pointers:
            if check:
                if target > nums[m]:    // if target is greater than the middle value, l = m
                    l = m+1
            if check:
                if target < nums[m]:    // if target is less than the middle value, r = m
                    r = m-1

    return:
        -1  // if outside the loop, target NOT in numsn neighbors list:

Example of 1st iterations:
    index:    0 1 2 3 4 5
    nums:   [-1,0,3,5,9,12]
    target: 9

    l = 0
    r = 5 (length-1)

    1st:      l   m     r
    index:    0 1 2 3 4 5
    range:  |-------------|
    nums:   [-1,0,3,5,9,12]
        l=0
        r=5
        m = 2 (l+r / 2) -> 0+5/2

        nums[2] = 3
        3 != target (9)

        target > r
        l = m+1
        l= 3

    2nd:            l m r
    index:    0 1 2 3 4 5
    range:         |------|
    nums:   [-1,0,3,5,9,12]
        l=3
        r=5
        m = 4 (l+r / 2) -> 3+5/2

        nums[4] = 9
        9 == target (9)

    RETURN m
"""


def binary_search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = int((l + r) / 2)

        if nums[m] == target:
            return m

        if target > nums[m]:
            l = m + 1
        if target < nums[m]:
            r = m - 1

    return -1


if __name__ == '__main__':
    arr = [-1, 0, 3, 5, 9, 12]
    find = 9

    print(arr)
    print("finding: " + str(find))
    print("index: " + str(binary_search(arr, find)))
