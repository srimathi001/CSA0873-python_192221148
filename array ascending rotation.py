def find_rotation_count(nums):
    left, right = 0, len(nums) - 1
    if nums[left] <= nums[right]:
        return 0
    while left < right:
        mid = (left + right) // 2
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid
    return left
nums = [3,4,5,1,2]
rotation_count = find_rotation_count(nums)
print("The array was rotated", rotation_count, "times.")
