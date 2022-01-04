def numIdenticalPairs(nums):
        count_ = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    count_ = count_ + 1
        return count_
