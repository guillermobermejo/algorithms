"""
Binary Search Algorithm Implementation (Recursive Version)

Programmer: Guillermo Bermejo

This implementation performs binary search on a sorted list to find the index of a target
value in an recursive manner. It repeatedly divides the search interval in half, leveraging
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
    if no l has been given (l is None):
        create l                        (set left pointer to start of array)

    if no r has been given (r is None):
        create r                        (set right pointer to end of array)

    if l > r:
        return                          (break recursion i.e., left passed right not in array)

    create middle value:
        m = int((l + r) / 2)            (middle is the sum of both pointers divided by 2)

    if nums[m] is the target:
        return m                        (the value at index m is the target)

    if target > nums[m]
        return binaru_search(nums, target, m + 1, r)

    if target < nums[m]
        return binaru_search(nums, target, l, m - 1)

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


def binary_search(nums, target, l=None, r=None):
    if l is None:
        l = 0
    if r is None:
        r = len(nums) - 1

    if l > r:
        return -1

    m = int((l + r) / 2)

    if nums[m] == target:
        return m

    if target > nums[m]:
        return binary_search(nums, target, m + 1, r)

    if target < nums[m]:
        return binary_search(nums, target, l, m - 1)


def binary_search_alternate(nums, target):
    def binary_search_helper(nums, target, l, r):
        if l > r:
            return -1

        m = int((l + r) / 2)

        if nums[m] == target:
            return m

        if target > nums[m]:
            return binary_search(nums, target, m + 1, r)

        if target < nums[m]:
            return binary_search(nums, target, l, m - 1)

    return binary_search_helper(nums, target, 0, len(nums) - 1)


if __name__ == '__main__':
    arr = [-1, 0, 3, 5, 9, 12]
    find = 9

    print(arr)
    print("finding: " + str(find))
    print("index: " + str(binary_search(arr, find)))
    print("index: " + str(binary_search_alternate(arr, find)))
