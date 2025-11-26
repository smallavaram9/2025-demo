def find_max(nums):
    if not nums:
        return None
    
    maximum = nums[0]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] > maximum:
                maximum = nums[j]
    return maximum
