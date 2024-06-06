def findDuplicate(nums):
    t = nums[0]
    h = nums[0]
    while True:
        t = nums[t]
        h = nums[nums[h]]
        if t == h:
            break
    ptr1 = nums[0]
    ptr2 = t
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))
