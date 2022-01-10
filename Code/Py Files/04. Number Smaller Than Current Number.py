def smallerNumbersThanCurrent(nums):
    # Approach 1: O(n^2)
    # For each element in nums
    # Check for all combinations and increment the count
    ls = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[j] < nums[i]:
                count += 1
        ls.append(count)
    return ls

    # Approach 2: O(n + log n) = O(n)
    # log n is complexity for sorted(array)
    # For each element in nums
    # Append their indices from the sorted nums_ array
    ls = []
    nums_ = sorted(nums)
    for i in nums:
        ls.append(nums_.index(i))
    return ls
