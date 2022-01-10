def numIdenticalPairs(nums):
    # Approach 1: O(n^2)
    # For each element in nums
    # Check for all combinations and increment the count
    count_ = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i < j:
                count_ = count_ + 1
    return count_
    
    # Approach 2: O(m+n)
    # Using defaultdict
    # n is size of array and m is size of duplicates in array
    # For each element in nums
    # Using default dict, update occurances of each element 
    # For values in dict, number of good pairs can be calculated by num(num-1)//2
    from collections import defaultdict
    count_ = 0
    d_ = defaultdict(int)

    for num in nums:
        if num in nums:
            d_[num] += 1

    for num in d_.values():
        count_ += (num*(num-1))//2
    return count_
