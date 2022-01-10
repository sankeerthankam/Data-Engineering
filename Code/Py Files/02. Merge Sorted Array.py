def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Approach 1: Three pointer approach
    p1, p2, p3 = m - 1, n - 1, len(nums1) - 1
    while p1 >= 0 and p2 >= 0:
        if nums2[p2] > nums1[p1]:
            nums1[p3] = nums2[p2]
            p2 -= 1
        else:
            nums1[p3] = nums1[p1]
            p1 -= 1
        p3 -= 1
    nums1[:p2 + 1] = nums2[:p2 + 1]
    
    
    # Approach 2: Using m and n instead of pointers
    last = m + n -1
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m = m - 1
        else:
            nums1[last] = nums2[n - 1]
            n = n - 1
        last = last - 1

    while n > 0:
        nums1[last] = nums2[n-1]
        n = n - 1
        last = last - 1

    return nums1
